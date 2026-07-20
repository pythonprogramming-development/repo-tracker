# My Awesome YouTube Channel

Welcome to my YouTube channel! 🎉 In this channel, I share exciting content related to web development. Whether you're interested in Angular, Javascript, or Productivity tips, you'll find something valuable here.
[YouTube Channel](http://youtube.com/@neweraofcoding)

## About Me

I'm Sam, and I'm passionate about product engineering and web development. I create videos that will help you learn web development.

## What You'll Find Here

- **[ Angular ]**: [Learn the fundamentals. I explained everything you need to get started with this JavaScript framework written in TypeScript. It is the web development framework for building the future. works at any scale. Loved by millions. Build for everyone.  open-source framework for building single-page client applications using HTML and TypeScript.]
- **[ Javascript ]**: [JavaScript is a powerful programming language that can add interactivity to a website. JavaScript is easy to learn. It's the foundation of frontend web development.]
- **[ Career Tips ]**: [self-assessment, goal setting, action planning, implementation, and refinement. By following these steps, you can develop a road map for achieving your career goals. Tips to improve your career development. Cultivating a beginner's mindset is a critical part of career growth. critical part of your professional growth.]
- **[ Common Errors ]**: [Mistakes to Avoid in Software Development Projects.]
- **[ Development Tools ]**: [Top Software Development Tools List.]
- **[ Typescript ]**: [TypeScript extends JavaScript by adding types to the language. TypeScript speeds up your development experience by catching errors. TypeScript can help enhance and improve your web development projects.]
- **[ Git & GitHub ]**: [GitHub is where over 100 million developers shape the future of software together. Contribute to the open-source community and manage Git repositories. This practical guide gets you to jump right into using GitHub, learning the basics of Git. Git and GitHub are two of the most essential tools in the world of software development.]
- **[ Video Conferencing Tool ]**: [Unlock the potential of video conferencing software development. Dive into our guide for insights on key features and cost factors.  If you're looking to integrate video communication into your app or planning to build a video streaming/conference app from scratch, create a fully customized audio & video conferencing app.]


### About the app - Multi-Repo Command Center
Moved from a simple script to a high-performance automation tool, and the core Python concepts we used to get there.
In modern software development, we rarely work on just one project. We have frontends, backends, microservices, and documentation repos. The "Multi-Repo Headache" occurs when you forget to push a critical fix in one folder while moving to another. 

This chapter explores how to use Python to build a **Local Repository Tracker**—a tool that scans hundreds of directories in seconds and provides a visual dashboard of your work.

### 1. The Engine: Interfacing with Git (`subprocess`)
The first thing we learned is that Python doesn't need to "re-invent" Git. Instead, it acts as a **driver**. We used the `subprocess` module to send commands to the system’s Git installation.

*   **The "Porcelain" Secret:** When scripts talk to Git, we use the `--porcelain` flag. While standard `git status` is designed to be "pretty" for humans, "porcelain" output is designed to be stable and easy for machines to parse. 
*   **The Logic:** If `git status --porcelain` returns an empty string, the repo is "Clean." If it returns any text at all, we know there are "Changes."

### 2. The Map: Navigating the Filesystem (`os` and `pathlib`)
To find your projects, Python has to "walk" through your hard drive. We explored two ways to do this:
*   **Shallow Scanning:** Looking only at the immediate folders inside a directory.
*   **Deep/Recursive Scanning:** Using `os.walk`, which dives into every sub-folder. 

The "signature" of a repository is the `.git` folder. By teaching our script to look for that specific hidden folder, it can distinguish between a random folder of cat pictures and a professional coding project.

### 3. The Dashboard: User Interface with `Rich`
Raw text data is hard to read. To make the tool useful, we used the **Rich** library to create a **Terminal User Interface (TUI)**.

*   **Visual Hierarchy:** We learned that colors aren't just for decoration—they are **status indicators**. 
    *   **Red** creates urgency (Uncommitted changes).
    *   **Yellow** signals a "pending" state (Unpushed commits).
    *   **Green** signals safety (Clean repo).
*   **Tables:** By using a structured table, we condensed 10 lines of Git output into a single, high-density row, allowing us to see the status of 50 repos on one screen.

### 4. Scaling Up: The Power of Concurrency (`Threaded Execution`)
When you have 5 or 10 repositories, a simple script is fast. When you have **100+ repositories**, checking them one-by-one (sequentially) becomes painfully slow because the script has to wait for the hard drive to respond for each repo.

We solved this using **Multi-threading** (`concurrent.futures`):
*   **Sequential:** Repo 1... (wait)... Repo 2... (wait)... Repo 3.
*   **Parallel:** Repo 1, 2, 3, 4, 5, 6, 7, 8, 9, 10... (all at once).

This is a "Pro" level optimization. It moves the bottleneck from the CPU to the I/O (Input/Output), making the script feel "instant" even with massive amounts of data.

### 5. Summary: The Automation Mindset
The most important lesson in this chapter isn't actually Python code—it's the **Automation Mindset**. 

Instead of manually typing `cd repo_name` and `git status` 100 times a day, we spent that time building a tool to do it for us. This reduces "Cognitive Load"—the mental energy spent remembering where you left off—allowing you to focus entirely on writing code.

---

### Key Takeaways for your "Developer Toolbox":
1.  **Don't Rebuild, Wrap:** Use Python to wrap existing CLI tools (like Git) to add new features.
2.  **UX Matters in the Terminal:** A well-formatted table with colors is 10x more effective than a wall of black-and-white text.
3.  **Speed through Parallelism:** When tasks involve waiting for the system (I/O bound), use threads to do many things at once.
4.  **Relative vs. Absolute Paths:** Use `os.path.abspath(__file__)` to make your scripts "portable" so they work no matter where you move them.

To run the project-
python tracker.py/py tracker.py 

TODO-
filter clean and red repos 
export in file

### Useful Links

###  APIs Detail
 
### Packages used

## Subscribe and Stay Updated!

Don't miss out on new videos! Subscribe to my channel and hit the notification bell 🔔 to receive updates whenever I upload fresh content. Let's learn, laugh, and explore together!

[!Subscribe to My Channel](http://youtube.com/@neweraofcoding)

## Connect with Me

- **YouTube**: [YouTube Channel Link](http://youtube.com/@neweraofcoding)
- **Facebook**: [Facebook Page Link](https://www.facebook.com/learnangular2plus/)
- **Instagram**: [Instagram Page Link](https://www.instagram.com/angular_development/)

Feel free to reach out, comment on videos, and share your thoughts. I appreciate your support! 🙌

## License

This project is licensed under the MIT License.

---

If you have any questions or need further assistance, feel free to ask! 🚀

##  Steps to contribute and generate PR(pull request)

 ###  clone the repository
clone the forked repository to your system. Go to your GitHub account, open the forked repository, click on the code button and then clone the repository.
If you want to use the terminal, use the following commands after you fork the repository, open the terminal type the given command
```
git clone repo url
```
### create a branch
 create a branch on your local repository to solve a problem.

Terminal commands
```
git checkout -b your_new_branch_name
```   
###   add & commit
add your changes(folder) to that branch.
Make necessary changes and commit those changes. Terminal commands
```
git add .
git commit -m "your-commit-message"
```
### push changes to github
finally, push your local repository to the remote repository compare & submit a pull request

terminal commands
```
git push origin 
```
Go to your repository on GitHub, you'll see a compare & pull request button. Click on that button.

Now submit the pull request.
   
For quick approval of the pull request, reach out to me on the mentioned social media channels.
```bash



 _____ _                 _     __   __            
|_   _| |               | |    \ \ / /            
  | | | |__   __ _ _ __ | | __  \ V /___  _   _   
  | | | '_ \ / _` | '_ \| |/ /   \ // _ \| | | |  
  | | | | | | (_| | | | |   <    | | (_) | |_| |  
  \_/ |_| |_|\__,_|_| |_|_|\_\   \_/\___/ \__,_|  
                                                  
                                                  
______                                            
|  ___|                                           
| |_ ___  _ __                                    
|  _/ _ \| '__|                                   
| || (_) | |                                      
\_| \___/|_|                                      
                                                  
                                                  
______      _               _   _               _ 
| ___ \    (_)             | | | |             | |
| |_/ / ___ _ _ __   __ _  | |_| | ___ _ __ ___| |
| ___ \/ _ \ | '_ \ / _` | |  _  |/ _ \ '__/ _ \ |
| |_/ /  __/ | | | | (_| | | | | |  __/ | |  __/_|
\____/ \___|_|_| |_|\__, | \_| |_/\___|_|  \___(_)
                     __/ |                        
                    |___/                         

 


```
---------
```javascript

if (youEnjoyed) {
 //  (star ⭐ & fork 🍽️) this repository.
 // - Fork this repository by clicking on the fork button at the top of this page. This will create a copy of this repository in your account.
    starThisRepository();
}

```
---------
happy coding fellas!!💕✨
-----------
 


