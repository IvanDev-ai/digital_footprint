import os
import shutil

def create_debian_structure():
    os.makedirs("debian/DEBIAN", exist_ok=True)
    
    control_content = """Package: digital-footprint
Version: 1.0
Architecture: all
Maintainer: TuNombre <tu@email.com>
Depends: python3, python3-requests, python3-bs4, python3-whois, python3-dnspython
Section: admin
Priority: optional
Description: Digital Footprint Scanner
"""
    with open("debian/DEBIAN/control", "w") as f:
        f.write(control_content)
    
    postinst_content = """#!/bin/bash
REPO_FILE="/etc/apt/sources.list.d/digital-footprint.list"
if [ ! -f "$REPO_FILE" ]; then
    echo "deb [trusted=yes] https://TU-USUARIO.github.io/digital-footprint-apt stable main" | tee "$REPO_FILE"
fi
apt update
"""
    with open("debian/DEBIAN/postinst", "w") as f:
        f.write(postinst_content)
    os.chmod("debian/DEBIAN/postinst", 0o755)

def build_deb_package():
    os.system("dpkg-deb --build debian")
    shutil.move("debian.deb", "digital-footprint-repo.deb")

if __name__ == "__main__":
    create_debian_structure()
    build_deb_package()
    print("✅ Paquete .deb creado: digital-footprint-repo.deb")
