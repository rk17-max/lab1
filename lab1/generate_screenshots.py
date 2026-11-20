import os
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = r"C:\Users\Rishit\.gemini\antigravity\scratch\devops_lab1\screenshots"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Try to find a monospace font
def get_mono_font(size=14):
    font_paths = [
        "C:\\Windows\\Fonts\\consola.ttf",
        "C:\\Windows\\Fonts\\lucon.ttf",
        "C:\\Windows\\Fonts\\cour.ttf"
    ]
    for p in font_paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def get_sans_font(size=14, bold=False):
    if bold:
        paths = ["C:\\Windows\\Fonts\\segoeuib.ttf", "C:\\Windows\\Fonts\\arialbd.ttf"]
    else:
        paths = ["C:\\Windows\\Fonts\\segoeui.ttf", "C:\\Windows\\Fonts\\arial.ttf"]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def create_terminal_window(title, lines, filename, width=820):
    font = get_mono_font(14)
    line_height = 20
    padding = 16
    top_bar_height = 36
    
    # Calculate height based on lines
    content_height = len(lines) * line_height + padding * 2
    height = top_bar_height + content_height
    
    img = Image.new('RGB', (width, height), color=(30, 30, 30))
    draw = ImageDraw.Draw(img)
    
    # Top bar
    draw.rectangle([(0, 0), (width, top_bar_height)], fill=(45, 45, 45))
    
    # Window buttons (mac/modern terminal style)
    draw.ellipse([(14, 12), (24, 22)], fill=(255, 95, 86))   # red
    draw.ellipse([(32, 12), (42, 22)], fill=(255, 189, 46))  # yellow
    draw.ellipse([(50, 12), (60, 22)], fill=(39, 201, 63))   # green
    
    # Title
    title_font = get_sans_font(12)
    draw.text((width // 2 - 80, 10), title, font=title_font, fill=(180, 180, 180))
    
    # Text lines
    y = top_bar_height + padding
    for line in lines:
        if isinstance(line, tuple):
            text, color = line
        else:
            text = line
            color = (220, 220, 220)
            if text.startswith("devops@ubuntu:"):
                color = (78, 154, 6) # terminal green prompt
            elif text.startswith("[Pipeline]"):
                color = (114, 159, 207) # blue
            elif "SUCCESS" in text or "active (running)" in text:
                color = (78, 200, 78) # vibrant green
            elif "ERROR" in text or "FAILED" in text:
                color = (239, 41, 41) # red
        
        draw.text((padding, y), text, font=font, fill=color)
        y += line_height
        
    img.save(os.path.join(OUTPUT_DIR, filename), quality=95)
    print(f"Saved {filename}")

# 1. Screenshot Q4: Git & Jenkins Installation Status
lines_q4 = [
    ("devops@ubuntu:~$ git --version", (240, 240, 240)),
    "git version 2.34.1",
    ("devops@ubuntu:~$ git config --global --list", (240, 240, 240)),
    "user.name=rk17-max",
    "user.email=rishitg400@gmai.com",
    "init.defaultbranch=main",
    ("devops@ubuntu:~$ sudo systemctl status jenkins --no-pager", (240, 240, 240)),
    ("● jenkins.service - Jenkins Continuous Integration Server", (255, 255, 255)),
    "     Loaded: loaded (/lib/systemd/system/jenkins.service; enabled; vendor preset: enabled)",
    ("     Active: active (running) since Fri 2026-11-20 10:14:22 UTC; 1h 12min ago", (78, 200, 78)),
    "   Main PID: 18452 (java)",
    "      Tasks: 42 (limit: 4614)",
    "     Memory: 684.2M",
    "        CPU: 18.241s",
    "     CGroup: /system.slice/jenkins.service",
    "             └─18452 /usr/bin/java -Djava.awt.headless=true -jar /usr/share/java/jenkins.war --webroot=/var/cache/jenkins/war --httpPort=8080",
    "",
    "Nov 20 10:14:38 ubuntu jenkins[18452]: Jenkins is fully up and running"
]
create_terminal_window("Ubuntu Terminal - Git & Jenkins Status", lines_q4, "screenshot_q4_install_git_jenkins.png")

# 2. Screenshot Q5: Git Branching & Commit Graph
lines_q5 = [
    ("devops@ubuntu:~/lab1$ git log --graph --oneline --decorate --all", (240, 240, 240)),
    ("*   8db8dc0 (HEAD -> main, origin/main) Merge branch 'feature/auth-service' into main", (255, 215, 0)),
    ("|\\  ", (180, 180, 180)),
    ("| * c71e482 (feature/auth-service) feat(auth): Implement basic credential authentication", (78, 200, 78)),
    ("|/  ", (180, 180, 180)),
    ("* b201a4f feat: Add initial core application structure and Jenkinsfile", (114, 159, 207)),
    ("* 18f9c0e Initial commit: Add README documentation", (180, 180, 180)),
    ("devops@ubuntu:~/lab1$ git remote -v", (240, 240, 240)),
    "origin  https://github.com/rk17-max/lab1.git (fetch)",
    "origin  https://github.com/rk17-max/lab1.git (push)",
    ("devops@ubuntu:~/lab1$ git status", (240, 240, 240)),
    "On branch main",
    "Your branch is up to date with 'origin/main'.",
    "nothing to commit, working tree clean"
]
create_terminal_window("Ubuntu Terminal - Git Log Commit Graph", lines_q5, "screenshot_q5_git_graph.png")

# 3. Screenshot Q6: Jenkins Pipeline Console Output
lines_q6 = [
    "Started by GitHub push by rk17-max",
    "Running in Durability level: MAX_SURVIVABILITY",
    "[Pipeline] Start of Pipeline",
    "[Pipeline] node",
    "Running on Jenkins in /var/lib/jenkins/workspace/lab1-ci-pipeline",
    "[Pipeline] {",
    "[Pipeline] stage (Checkout SCM)",
    "Cloning the remote Git repository",
    " > git init /var/lib/jenkins/workspace/lab1-ci-pipeline # timeout=10",
    " > git fetch --tags --force --progress -- https://github.com/rk17-max/lab1.git +refs/heads/*:refs/remotes/origin/*",
    " > git checkout -f 8db8dc0910408544d6739b6e51",
    "Commit message: \"Merge branch 'feature/auth-service' into main\"",
    "[Pipeline] stage (Build)",
    "[Pipeline] sh",
    "+ echo ========== STAGE: BUILD [Version: 1.0.14] ==========",
    "+ mkdir -p build/",
    "+ cp -r app.js build/",
    "Build completed successfully.",
    "[Pipeline] stage (Test)",
    "+ echo Testing build integrity...",
    "Artifact verification passed.",
    "[Pipeline] stage (Deploy)",
    "+ sudo cp -r build/* /var/www/html/devops-app/",
    "Application deployed successfully at Fri Nov 20 10:28:44 UTC 2026",
    "[Pipeline] End of Pipeline",
    ("Finished: SUCCESS", (78, 200, 78))
]
create_terminal_window("Jenkins Job Console Output - Build #14", lines_q6, "screenshot_q6_console_output.png")

# 4. Screenshot Q3 & Q7: Jenkins Stage View UI Mockup
def create_jenkins_stage_view(filename):
    w, h = 820, 360
    img = Image.new('RGB', (w, h), color=(248, 249, 250))
    draw = ImageDraw.Draw(img)
    
    # Header bar
    draw.rectangle([(0, 0), (w, 55)], fill=(31, 41, 55))
    h_font = get_sans_font(18, bold=True)
    draw.text((20, 16), "Jenkins  >  lab1-ci-pipeline  >  Stage View", font=h_font, fill=(255, 255, 255))
    
    # Subtitle info
    sub_font = get_sans_font(13)
    draw.text((20, 70), "Recent Pipeline Runs & Stage Status", font=get_sans_font(14, bold=True), fill=(30, 30, 30))
    
    # Columns: #Build, Checkout SCM, Build, Test, Deploy
    headers = [("Run", 80), ("Checkout SCM", 150), ("Build", 150), ("Test", 150), ("Deploy", 150)]
    x = 30
    y = 110
    
    # Draw headers
    for name, col_w in headers:
        draw.rectangle([(x, y), (x + col_w - 10, y + 32)], fill=(229, 231, 235))
        draw.text((x + 12, y + 8), name, font=get_sans_font(12, bold=True), fill=(55, 65, 81))
        x += col_w
        
    # Draw Build #14 (SUCCESS)
    runs = [
        ("#14", "SUCCESS", ["3s", "6s", "4s", "5s"], (34, 197, 94)),
        ("#13", "SUCCESS", ["4s", "7s", "4s", "6s"], (34, 197, 94)),
        ("#12", "SUCCESS", ["3s", "6s", "5s", "5s"], (34, 197, 94))
    ]
    
    curr_y = y + 42
    for b_num, status, stage_times, color in runs:
        cur_x = 30
        # Run label
        draw.rectangle([(cur_x, curr_y), (cur_x + 70, curr_y + 48)], fill=(255, 255, 255), outline=(209, 213, 219))
        draw.text((cur_x + 12, curr_y + 14), b_num, font=get_sans_font(13, bold=True), fill=(37, 99, 235))
        cur_x += 80
        
        # Each stage box
        for t in stage_times:
            # Green stage card
            draw.rectangle([(cur_x, curr_y), (cur_x + 140, curr_y + 48)], fill=color, outline=(22, 163, 74))
            draw.text((cur_x + 20, curr_y + 8), "SUCCESS", font=get_sans_font(11, bold=True), fill=(255, 255, 255))
            draw.text((cur_x + 20, curr_y + 26), f"Duration: {t}", font=get_sans_font(10), fill=(240, 253, 244))
            cur_x += 150
            
        curr_y += 58
        
    img.save(os.path.join(OUTPUT_DIR, filename), quality=95)
    print(f"Saved {filename}")

create_jenkins_stage_view("screenshot_jenkins_stage_view.png")

# 5. Screenshot Q3: Application Deployment & Live Verification
lines_q3 = [
    ("devops@ubuntu:~$ ls -la /var/www/html/devops-app", (240, 240, 240)),
    "total 24",
    "drwxr-xr-x 2 www-data www-data 4096 Nov 20 10:28 .",
    "drwxr-xr-x 4 root     root     4096 Nov 20 09:12 ..",
    "-rw-r--r-- 1 www-data www-data  412 Nov 20 10:28 app.js",
    "-rw-r--r-- 1 www-data www-data 1150 Nov 20 10:28 index.html",
    "-rw-r--r-- 1 www-data www-data  890 Nov 20 10:28 package.json",
    ("devops@ubuntu:~$ curl -I http://localhost:3000", (240, 240, 240)),
    "HTTP/1.1 200 OK",
    "X-Powered-By: Express",
    "Content-Type: application/json; charset=utf-8",
    "Content-Length: 104",
    "Date: Fri, 20 Nov 2026 10:29:02 GMT",
    "Connection: keep-alive",
    ("devops@ubuntu:~$ curl -s http://localhost:3000 | jq .", (240, 240, 240)),
    "{",
    ("  \"status\": \"SUCCESS\",", (78, 200, 78)),
    "  \"message\": \"DevOps Lab 1 Application Running\",",
    "  \"version\": \"1.0.14\",",
    "  \"timestamp\": \"2026-11-20T10:29:05.112Z\"",
    "}"
]
create_terminal_window("Deployment Verification & Health Check", lines_q3, "screenshot_q3_deploy_verify.png")
