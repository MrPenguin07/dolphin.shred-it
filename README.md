# Dolphin-shredder
Dolphin right click context menu -> Shred files/dir

Dependencies: 
- Dolphin
- notify2
- tqdm
- GTK
- shred (Gentoo: sys-apps/coreutils)

## INSTALL
$ git clone https://github.com/MrPenguin07/dolphin-shredder.git && cd dolphin-shredder
$ sudo cp usr/share/kio/servicemenus/* /usr/share/kio/servicemenus/
$ sudo chmod +x /usr/share/kio/servicemenus/shred.py

Add the context menu in dolphin settings;
![image](https://github.com/MrPenguin07/dolphin-shredder/assets/127086564/505c97c7-68d0-4bd8-8b23-ea14f575a244)

GTK confirmation;
![image](https://github.com/MrPenguin07/dolphin-shredder/assets/127086564/fff57eb0-093f-479a-8999-6eff431f463d)

May also be run from the shell;
$ shred.py <file/dir>
