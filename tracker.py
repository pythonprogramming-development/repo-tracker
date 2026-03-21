import os
import subprocess
import concurrent.futures # For speed with 100s of repos
from rich.console import Console
from rich.table import Table
from rich.progress import Progress

# Search depth: 1 = same folder only, 2 = one folder deep, etc.
MAX_DEPTH = 3 
# Folder to search (default is where the script is)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

console = Console()

def is_git_repo(path):
    """Checks if a path is a git repo (handles folders, files, and bare repos)."""
    # Standard or Worktree/Submodule
    if os.path.exists(os.path.join(path, ".git")):
        return True
    # Bare repository (contains HEAD and config but no .git folder)
    if os.path.exists(os.path.join(path, "HEAD")) and os.path.exists(os.path.join(path, "config")):
        return True
    return False

def run_git_cmd(repo_path, args):
    try:
        result = subprocess.run(
            ["git", "-C", repo_path] + args,
            capture_output=True, text=True, check=True, timeout=5
        )
        return result.stdout.strip()
    except Exception:
        return None

def get_single_repo_data(path):
    """Gathers data for one specific repository."""
    name = os.path.basename(path)
    # Check if we are in a subfolder, show relative path if so
    rel_path = os.path.relpath(path, ROOT_DIR)
    
    branch = run_git_cmd(path, ["rev-parse", "--abbrev-ref", "HEAD"])
    status = run_git_cmd(path, ["status", "--porcelain"])
    unpushed = run_git_cmd(path, ["log", "@{u}..HEAD", "--oneline"])
    stashes = run_git_cmd(path, ["stash", "list"])
    
    return {
        "name": rel_path if rel_path != "." else name,
        "branch": branch or "N/A",
        "changes": len(status.splitlines()) if status else 0,
        "unpushed": len(unpushed.splitlines()) if unpushed else 0,
        "stashes": len(stashes.splitlines()) if stashes else 0
    }

def find_repos(root, max_depth):
    """Finds all git repositories up to a certain depth."""
    repos = []
    root = os.path.abspath(root)
    base_depth = root.count(os.sep)
    
    for dirpath, dirnames, filenames in os.walk(root):
        current_depth = dirpath.count(os.sep) - base_depth
        if current_depth >= max_depth:
            del dirnames[:] # Don't go deeper
            continue
            
        if is_git_repo(dirpath):
            repos.append(dirpath)
            del dirnames[:] # Don't search inside a repo for other repos
    return repos

def main():
    console.print(f"[bold blue]Scanning for Repositories in:[/bold blue] {ROOT_DIR}\n")
    
    repo_paths = find_repos(ROOT_DIR, MAX_DEPTH)
    
    if not repo_paths:
        console.print("[bold red]No repositories found![/bold red]")
        return

    table = Table(title=f"Tracker: {len(repo_paths)} Repositories Found")
    table.add_column("Repository", style="cyan", no_wrap=True)
    table.add_column("Branch", style="magenta")
    table.add_column("Changes", justify="right")
    table.add_column("Unpushed", justify="right")
    table.add_column("Stashes", justify="right")

    # Use ThreadPoolExecutor to run Git commands in parallel (much faster for 100+ repos)
    with Progress() as progress:
        task = progress.add_task("[green]Checking status...", total=len(repo_paths))
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            future_to_repo = {executor.submit(get_single_repo_data, path): path for path in repo_paths}
            
            for future in concurrent.futures.as_completed(future_to_repo):
                data = future.result()
                
                # Format the row
                change_str = f"[bold red]Yes ({data['changes']})" if data['changes'] > 0 else "[green]Clean"
                push_str = f"[bold yellow]{data['unpushed']}" if data['unpushed'] > 0 else "[dim]0"
                stash_str = f"{data['stashes']}" if data['stashes'] > 0 else "[dim]0"
                
                table.add_row(data['name'], data['branch'], change_str, push_str, stash_str)
                progress.update(task, advance=1)

    console.print(table)

if __name__ == "__main__":
    main()