# About
This program is used to extract the mod id's from the .html modpacks that the Arma3 launcher provides. <br>
**Detailed explanation:** Every Arma3 modpack is a `.html` that has links to the mods in it that looks something like this:
```
https://steamcommunity.com/sharedfiles/filedetails/?id=450814997
```
The program takes the `id` from the end of the link and saves it to a file specified by the user. This operation is repeated for every mod in the modpack. 

# Building the program
I don't really know how to compile this program correctly on other systems but this is how I do it on my Arch Linux operating system:
```bash
cd build/
cmake --build ../build/
./ArmaExtractorGUI
```
I'll update this README file in the future.