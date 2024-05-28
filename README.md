# 漏洞扫描系统

## 设计目的：

* 使学生深入理解和掌握漏洞扫描系统的原理、技术和应用，提高网络安全防护能力。
* 使学生能够掌握漏洞扫描的基本概念、原理和方法，了解漏洞扫描系统的组成和功能，以及常见的漏洞类型和攻击方式。
* 培养学生具备使用漏洞扫描工具进行网络安全检测和评估的能力，包括扫描策略的制定、扫描过程的执行、扫描结果的分析和漏洞修复建议的提出等。
* 通过案例分析和实践操作，培养学生的网络安全意识和思维，使其能够独立思考和解决网络安全问题，提高网络安全防护的主动性和有效性。
* 使学生了解网络安全法规和标准，掌握如何利用漏洞扫描系统帮助组织遵守相关法规和标准的要求，确保系统的合规性。

## 设计要求

利用Python语言实现一个漏洞扫描系统，需包括以下功能：

1. 主机漏洞扫描：通过端口扫描、主机发现（Ping命令、ARP请求或ICMP请求）等技术，识别网络中的活跃主机和开放端口，识别可能存在的服务；对已识别的服务进行深入扫描，检测可能存在的安全漏洞，如XSS、SQL 注入、弱口令、缓冲区溢出等。(1人)
2. WEB网页漏洞扫描：编写爬虫程序收集网页数据，利用漏洞检测库和正则表达式等技术，收集到的信息进行深入的分析和匹配，检测常见的Web应用程序漏洞类型，如SQL注入、XSS、CSRF等。(1人)
3. 数据库管理：所有扫描数据、用户数据、日志数据、配置信息都使用数据库保存，可通过用户界面进行数据的增删改查。(1人)
4. 用户交互模块：提供友好的用户界面，用户可以通过界面配置系统参数，如目标网络，目标网站的URL、扫描参数、报告格式、漏洞库设置或更新等。所有扫描结果通过界面进行图形化展示，实时显示漏洞数量、严重程度等信息
5. 漏洞报告模块：综合上面两个漏洞扫描模块，对漏洞进行分类和评级，自动生成详细的漏洞报告，包括漏洞类型、影响范围、漏洞描述、修复建议等信息。报告可以HTML、PDF或其他格式输出，方便用户查阅。另外，报告也可以供用户下载。（1人）
6. 用户管理模块：用户注册、登录，实现用户身份验证和权限控制，根据用户角色或权限，限制其对系统的访问和操作范围，只有授权用户才能访问系统并进行漏洞扫描。
7. 日志记录模块：记录系统运行过程中的关键事件和错误信息，可导出日志文件。
8. 修复评估模块：根据漏洞的类型、危害等级以及被利用的风险等因素，为用户提供针对性的修复建议。这些建议可能包括更新软件版本、修补安全补丁、调整系统配置等。(1人)

## 设计实现

单独的模块：主机漏洞扫描、WEB网页漏洞扫描、

使用Django完成：数据库管理、用户交互、

