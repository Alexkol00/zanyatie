FROM python:3.12-slim
WORKDIR /app
COPY solutions/mission.py ./mission.py
ENTRYPOINT ["python", "mission.py"]
CMD ["--battery", "60", "--max-risk", "4"]
