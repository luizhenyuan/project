# 幼小衔接课程应用 - 部署指南

## 📋 部署顺序概览

| 步骤 | 组件 | 优先级 | 说明 |
|------|------|--------|------|
| 1 | 操作系统环境准备 | 高 | 更新系统、安装基础依赖 |
| 2 | MariaDB 数据库 | 高 | 数据持久化核心 |
| 3 | Python 环境 & 后端依赖 | 高 | FastAPI 运行环境 |
| 4 | 后端 API 服务 | 高 | 业务逻辑处理 |
| 5 | 前端构建 & 部署 | 高 | 用户界面展示 |
| 6 | Nginx 反向代理（可选） | 中 | 生产环境推荐 |
| 7 | 验证测试 | 高 | 确保服务正常 |

---

## 🚀 第一步：操作系统环境准备

### 1.1 更新系统（Ubuntu/Debian）
```bash
# 更新软件源
sudo apt-get update && sudo apt-get upgrade -y

# 安装基础工具
sudo apt-get install -y git vim wget curl build-essential
```

### 1.2 安装 Python 3.10+
```bash
# 安装 Python
sudo apt-get install -y python3 python3-pip python3-dev

# 验证版本
python3 --version  # 要求 >= 3.10
```

---

## 🚀 第二步：MariaDB 数据库部署

### 2.1 安装 MariaDB
```bash
# 安装 MariaDB 服务器
sudo apt-get install -y mariadb-server mariadb-client

# 启动服务
sudo systemctl start mariadb
sudo systemctl enable mariadb
```

### 2.2 配置数据库
```bash
# 进入 MySQL/MariaDB 命令行
mysql -u root

# 创建数据库
CREATE DATABASE preschool_app CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# 创建用户
CREATE USER 'preschool'@'localhost' IDENTIFIED BY 'YourStrongPassword123!';

# 授权
GRANT ALL PRIVILEGES ON preschool_app.* TO 'preschool'@'localhost';
FLUSH PRIVILEGES;

# 退出
EXIT;
```

### 2.3 验证数据库连接
```bash
mysql -u preschool -p preschool_app -e "SELECT 1;"
# 输入密码后应返回 1
```

---

## 🚀 第三步：后端服务部署

### 3.1 克隆项目
```bash
# 进入项目目录
mkdir -p /opt/preschool-app && cd /opt/preschool-app

# 克隆代码（如果使用 Git）
git clone <your-repo-url> .

# 或者直接使用现有代码
# cp -r /workspace/preschool-app/* .
```

### 3.2 安装依赖
```bash
cd backend

# 安装 Python 依赖
pip install -r requirements.txt

# 如果没有 requirements.txt，手动安装：
pip install fastapi uvicorn sqlalchemy pymysql python-jose passlib bcrypt
```

### 3.3 配置数据库连接
编辑以下文件，修改数据库连接字符串：

- [app/routes/auth.py](file:///workspace/preschool-app/backend/app/routes/auth.py#L11)
- [app/routes/course.py](file:///workspace/preschool-app/backend/app/routes/course.py#L10)
- [app/routes/practice.py](file:///workspace/preschool-app/backend/app/routes/practice.py#L11)

```python
# 修改为你的数据库配置
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://preschool:YourStrongPassword123!@localhost:3306/preschool_app"
```

### 3.4 启动后端服务

**开发模式（调试用）：**
```bash
cd /opt/preschool-app/backend
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

**生产模式（推荐）：**
```bash
# 使用 nohup 后台运行
nohup python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 > /var/log/preschool-backend.log 2>&1 &
```

**使用 systemd 服务（推荐）：**
```bash
# 创建 systemd 服务文件
sudo cat > /etc/systemd/system/preschool-backend.service << EOF
[Unit]
Description=Preschool App Backend Service
After=network.target mariadb.service

[Service]
User=www-data
WorkingDirectory=/opt/preschool-app/backend
ExecStart=/usr/bin/python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

# 启动服务
sudo systemctl daemon-reload
sudo systemctl start preschool-backend
sudo systemctl enable preschool-backend
```

### 3.5 验证后端服务
```bash
# 健康检查
curl http://localhost:8000/api/health
# 应返回: {"status":"ok","message":"幼小衔接课程应用 API 运行正常"}

# 获取课程列表
curl http://localhost:8000/api/courses
```

---

## 🚀 第四步：前端应用部署

### 4.1 安装 Node.js
```bash
# 安装 Node.js 18+
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# 验证版本
node --version  # 要求 >= 18.0.0
npm --version
```

### 4.2 安装依赖并构建
```bash
cd /opt/preschool-app/frontend

# 安装依赖
npm install

# 构建生产版本
npm run build
```

### 4.3 配置 API 地址
编辑 `.env` 文件配置后端 API 地址：
```bash
# .env 文件内容
VITE_API_URL=http://localhost:8000/api
```

### 4.4 部署前端

**方式一：使用 Vite 开发服务器（调试用）**
```bash
cd /opt/preschool-app/frontend
npm run dev -- --host 0.0.0.0 --port 5173
```

**方式二：使用静态文件服务（生产用）**
```bash
# 安装 serve
npm install -g serve

# 启动静态服务
serve -s dist -l 5173
```

---

## 🚀 第五步：Nginx 反向代理（生产环境）

### 5.1 安装 Nginx
```bash
sudo apt-get install -y nginx
```

### 5.2 配置 Nginx

创建配置文件 `/etc/nginx/sites-available/preschool-app`：
```nginx
server {
    listen 80;
    server_name your-domain.com;

    # 前端静态文件
    location / {
        root /opt/preschool-app/frontend/dist;
        try_files $uri $uri/ /index.html;
    }

    # API 反向代理
    location /api/ {
        proxy_pass http://localhost:8000/api/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    # 错误页面
    error_page 404 /index.html;
}
```

### 5.3 启用配置
```bash
# 创建软链接
sudo ln -s /etc/nginx/sites-available/preschool-app /etc/nginx/sites-enabled/

# 测试配置
sudo nginx -t

# 重启 Nginx
sudo systemctl restart nginx
```

---

## 🚀 第六步：验证与测试

### 6.1 服务状态检查
```bash
# 检查后端服务
sudo systemctl status preschool-backend

# 检查 Nginx
sudo systemctl status nginx

# 检查 MariaDB
sudo systemctl status mariadb
```

### 6.2 API 测试
```bash
# 健康检查
curl http://localhost/api/health

# 获取课程列表
curl http://localhost/api/courses

# 获取学科分类
curl http://localhost/api/courses/subjects

# 用户注册测试
curl -X POST http://localhost/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"testpass123"}'

# 用户登录测试
curl -X POST http://localhost/api/auth/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=testuser&password=testpass123"
```

### 6.3 前端访问
在浏览器中访问：
- 开发环境：`http://localhost:5173`
- 生产环境：`http://your-domain.com`

---

## ⚠️ 注意事项

### 安全建议
1. **密码安全**：不要使用默认密码，修改 `YourStrongPassword123!` 为强密码
2. **防火墙配置**：仅开放必要端口（80, 443）
3. **HTTPS**：生产环境配置 SSL 证书（使用 Let's Encrypt）
4. **权限控制**：限制数据库用户权限，不要使用 root 用户

### 日志管理
```bash
# 后端日志
tail -f /var/log/preschool-backend.log

# Nginx 日志
tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log
```

### 常见问题

**Q1: 数据库连接失败**
```bash
# 检查数据库服务
sudo systemctl status mariadb

# 检查数据库配置
mysql -u preschool -p preschool_app -e "SELECT 1;"
```

**Q2: 端口占用**
```bash
# 查看端口占用
netstat -tlnp | grep 8000
netstat -tlnp | grep 5173

# 杀死占用进程
kill -9 <PID>
```

**Q3: Nginx 配置错误**
```bash
# 测试配置
nginx -t

# 查看错误日志
tail -f /var/log/nginx/error.log
```

---

## 📁 项目结构

```
preschool-app/
├── backend/                    # 后端服务
│   ├── app/                    # 应用代码
│   │   ├── main.py             # 入口文件
│   │   ├── models.py           # 数据库模型
│   │   ├── schemas.py          # 数据结构
│   │   ├── routes/             # API 路由
│   │   └── utils/              # 工具函数
│   └── test.db                 # SQLite（开发环境）
├── frontend/                   # 前端应用
│   ├── src/                    # 源代码
│   ├── dist/                   # 构建产物
│   ├── package.json            # 依赖配置
│   └── vite.config.js          # Vite 配置
└── deployment_guide.md         # 部署指南
```

---

## 📝 部署清单

- [ ] 操作系统更新完成
- [ ] MariaDB 安装配置完成
- [ ] 后端依赖安装完成
- [ ] 后端服务启动正常
- [ ] 前端依赖安装完成
- [ ] 前端构建完成
- [ ] Nginx 配置完成（可选）
- [ ] API 测试通过
- [ ] 前端访问正常
