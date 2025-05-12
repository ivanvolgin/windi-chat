FROM ubuntu:latest
LABEL authors="ivanvolgin"

ENTRYPOINT ["top", "-b"]