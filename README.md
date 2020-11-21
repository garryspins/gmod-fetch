<p align="center">
  <img src="https://cdn.discordapp.com/attachments/767658460979527690/779505284527161364/unknown.png" alt="Logo" width="400" height="auto">
</p>

# GFetch

GFetch is a multi-purpose, highly extensible system information commandline interface for Garry's Mod.<br>
With overcomplicated CLI features it promises to be fun for 10 minutes then youll forget its there.


<details>
<summary>Features</summary>
  
- Easy, Clean, Object Based API.
- Provides Easy Access to Useful Information.
- Neat Map Image.
- Licensed under GPLv3, if it doesnt have a feature youd like you can add it.
</details>

<details>
<summary>Basic Usage</summary>

Just type `gfetch` in console and itll do its thing.
 
For more advanced commands type `-h` as an option

</details>

<details>
<summary>Documentation</summary>
  
  If you dont understand a function look at the gfetch_modules directory for examples.
   #### GFetch Methods
   ---
  `GFetch:AddModule(Str name,Str short)` : Creates a Module : Shared<br>
  
  `String name`  :  Full Name of the module (aka 'Pretty Name')<br>
  `String short` :  Short Name of the module, This is the name that people will see and use to disable it in the commandline<br>
   <br>
   Returns       :  ModuleObj
  
  
  `GFetch:AddCommand(Str full,Str short,Str desc,Func func,Bool blocking)` : Creates a command : Shared<br>
  `String full`  :  Full Command (Should start with `--`)<br>
  `String short` :  Short Command (Should start with `-`)<br>
  `String Descr` :  Description<br>
  `Func Func`    :  The commands function - Called with the current running commands configurations, Next argument<br>
  `Bool Blocking`:  Should the command block the output of the fetch, this can also be done by returning `true` from the `Func` argument<br>
   <br>
   <br>
   <br>
   #### ModuleObj Methods
   ---
   ! Means Set or Get.<br><br>
   
   Name of the Module<br>
   `!Name()`<br><br>
   Short Name of the Module<br>
   `!Short()`<br><br>
   Description of the Module<br>
   `!Description()`<br><br>
   Function of the Module<br>
   `!Function()`<br><br>
   State that the Module should be ran on (CLIENT/SERVER)<br>
   `!State()`<br><br>
</details>
<details>
<summary>Images</summary>
  <p align="center">
<p><img src="https://cdn.discordapp.com/attachments/517937376073482251/779518121240166420/unknown.png" alt="Image"> </p>
<p><img src="https://cdn.discordapp.com/attachments/517937376073482251/779518366469455892/unknown.png" alt="Image"> </p>
<p><img src="https://cdn.discordapp.com/attachments/517937376073482251/779518515060801577/unknown.png" alt="Image"> </p>
<p><img src="https://cdn.discordapp.com/attachments/517937376073482251/779518715091615765/unknown.png" alt="Image"> </p>
<p><img src="https://cdn.discordapp.com/attachments/517937376073482251/779518836373585940/unknown.png" alt="Image"> </p>
<p><img src="https://cdn.discordapp.com/attachments/517937376073482251/779518912823820318/unknown.png" alt="Image"> </p>
<p><img src="https://cdn.discordapp.com/attachments/517937376073482251/779518986861412412/unknown.png" alt="Image"> </p>
<p><img src="https://cdn.discordapp.com/attachments/517937376073482251/779519085545127976/unknown.png" alt="Image"> </p>
<p><img src="https://cdn.discordapp.com/attachments/517937376073482251/779519206731022336/unknown.png" alt="Image"></p>

  </p>
  
</details>

