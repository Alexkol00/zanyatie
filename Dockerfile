FROM python:3.12-slim
WORKDIR /app
COPY mission.py .
ENTRYPOINT ["python", "mission.py"]
CMD ["--battery", "60", "--max-risk", "4"]
