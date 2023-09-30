# Dolphin-shredder
Dolphin right click context menu -> Shred files/dir

Securely delete your files from within the Dolphin file manager!

Dependencies: 
- Dolphin
- notify2
- tqdm
- GTK
- shred (Gentoo: sys-apps/coreutils)

## INSTALL
```
$ git clone https://github.com/MrPenguin07/dolphin-shredder.git && cd dolphin-shredder
$ sudo cp usr/share/kio/servicemenus/* /usr/share/kio/servicemenus/
$ sudo chmod +x /usr/share/kio/servicemenus/shred.py
```
Add the context menu in dolphin settings;

![image](https://github.com/MrPenguin07/dolphin-shredder/assets/127086564/505c97c7-68d0-4bd8-8b23-ea14f575a244)

Right-click context menu;

![image](https://github.com/MrPenguin07/dolphin-shredder/assets/127086564/7736015e-c175-456a-9a78-7229b60e6895)

GTK confirmation;

![image](https://github.com/MrPenguin07/dolphin-shredder/assets/127086564/fff57eb0-093f-479a-8999-6eff431f463d)

May also be run from the shell;

$ python3 shred.py <file/dir>

### Notes
_The default is 5 passes, can be changed within shred.py_

Todo: Update to gtk4 - or Qt would make more sense :)
