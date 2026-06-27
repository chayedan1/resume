# resume-builder

Flask + PostgreSQL 的简历制作与查看网站（前后端不分离）。

## 运行准备

1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
2. 配置数据库（默认 PostgreSQL）：
   ```bash
   set DATABASE_URL=postgresql+psycopg2://user:pass@host:5432/dbname
   ```
3. 初始化数据库表：
   ```bash
   flask --app run.py shell -c "from app import db; from app.models.user import User; db.create_all(); print('ok')"
   ```
4. 启动开发服务器：
   ```bash
   python run.py
   ```
