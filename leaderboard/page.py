class Page:
    def __init__(self, path: str):
        self.path = path
        self.content = ""

    def add_content(self, content: str):
        self.content += content

    def write(self):
        with open(self.path, 'w') as f:
            f.write(self.content)

    def set_header(self):
        self.content += """---
layout: default
---

[ ![Logo](https://kanziebub.github.io/ProjectSEA/assets/images/bullet_rev.png) Home](https://kanziebub.github.io/ProjectSEA/)
"""

    def set_footer(self):
        self.content += """
[ ![Logo](https://kanziebub.github.io/ProjectSEA/assets/images/bullet_rev.png) Home](https://kanziebub.github.io/ProjectSEA/)
"""
