# Booteroids 1 & 2

A clone of the classic Asteroids game, created as part of the [boot.dev Build Asteroids Python course](https://www.boot.dev/courses/build-asteroids-python). 
This project is split into two iterations—Booteroids 1 and Booteroids 2—with each version offering its own unique gameplay experience.

[Booteroids 1 Gameplay](https://www.youtube.com/watch?v=q8oH3w_ElB8)

[Booteroids 2 Gameplay](https://www.youtube.com/watch?v=5zmQxFuaMYw)

## Project Overview

Booteroids 1 is a fun, arcade-style game built in Python where you get to shoot at the instructors and various employees of boot.dev as their mascot "boots", this was
a guided project both completed in about 10 hours. 

The first iteration (Booteroids 1) delivers a straightforward, engaging gameplay experience, 
while Booteroids 2 adds more realistic physics but doesn't quite capture the feel of the original. While I’m really happy with how Booteroids 1 turned out, there’s always room for 
improvement. 

If I were to revisit it, I’d love to add “boots” as bullets. I’m also pleased with the ship’s acceleration and overall physics feel, but 
I’ve grown a bit tired of squashing the bugs I introduced by updating the physics while following a the unidirectional “VIP” pattern (View-Interactor-Presenter). 
This refactoring made updating the game physics easier to grok but introduced a bug to asteroid spawning and collision detection. For more details on the VIP pattern, check out this 
[article](https://dev.to/binoy123/architectural-pattern-vip-view-interactor-presenter-6hf). I just happened to read article the day that I 
was doing this project and wanted to retain what I read by building something with the pattern. Booteroids 1 took a wopping 6 hours to complete from start to finish, while 
Booteroids 2 was done in 4 hours. 

## Setupn

Before running the game, make sure you have Python 3 installed on your system.

1. **Clone the Repository**
   ```bash
   git clone https://github.com/jakemckenzie/booteroids.git
   cd booteroids
   ```
2. **Setup the Virtual Environment Run the provided bash script to set up the virtual environment:**

```bash
Copy
./run.sh
```
This script will create and activate a virtual environment with all necessary dependencies installed.
## Running the Project
### Booteroids 1
To start the original of the game (Booteroids 1), run:
```bash
python3 main.py
```
### Booteroids 2
To launch the sequel (Booteroids 2), use the following command:
```bash
python3 -m booteroids.view.game_view
```
## Developer Notes & Future Improvements
### Booteroids 1 Feedback:
I’m really happy with the initial version of the game. The ship acceleration and physics deliver a satisfying gameplay feel. 
However, if I were to revisit the project, I’d love to experiment with adding “boots” as bullets I came up with in the sequel.

### Challenges with Booteroids 2:
While Booteroids 2 builds on the original idea, migrating to the VIP (View-Interactor-Presenter) pattern introduced some 
challenges. In particular, updating the gameplay loop logic has become a bit cumbersome due to the unidirectional data flow. My asteroids aren't spawning 
as I expect them to and collision detection needs to be fixed but I'm happy with the "boots" as bullets feature and ship mechanics (now with acceleration!)
turned out fairly sick.

### Acknowledgments
[boot.dev/](https://www.boot.dev/) for the excellent course and resources.

I wasn't trying to shit on that VIP pattern or that article, I used this as an oppurtunity to try to retain the information I was injesting. Thank you Binoy Vijayan
for writing the article and [Danijela Vrzan](https://www.kodeco.com/29416318-getting-started-with-the-vip-clean-architecture-pattern) for writing the articles. Any bugs are 
my own skills issue and I take credit for that.
