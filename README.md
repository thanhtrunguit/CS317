
<p align="center">
  <a href="https://www.uit.edu.vn/" title="Trường Đại học Công nghệ Thông tin" style="border: 5;">
    <img src="https://i.imgur.com/WmMnSRt.png" alt="Trường Đại học Công nghệ Thông tin | University of Information Technology">
  </a>
</p>

<!-- Title -->
<h1 align="center"><b>CS317.P21 - PHÁT TRIỂN VÀ VẬN HÀNH HỆ THỐNG MÁY HỌC</b></h1>

## COURSE INTRODUCTION
<a name="gioithieumonhoc"></a>
* *Course Title*: Phát triển và vận hành hệ thống máy học
* *Course Code*: CS317.P21
* *Year*: 2024-2025

## ACADEMIC ADVISOR
<a name="giangvien"></a>
* *Đỗ Văn Tiến* - tiendv@uit.edu.vn
* *Lê Trần Trọng Khiêm* - khiemltt@uit.edu.vn

## MEMBERS
<a name="thanhvien"></a>
* Nguyễn Đình Vũ - 22521692
* Ngô Thành Trung - 22521560
* Đinh Nhật Trường - 22521575

---
# CS317: Lab 2 – API, Docker and Deploy API

This project is part of the **CS317** course and demonstrates a full **machine learning workflow** using **FastAPI**, **Docker** and **Remote Server** to create and deploy usable **API**. 

---


## 🧠 Pipeline Structure

Built using [FastAPI](https://fastapi.tiangolo.com/), the pipeline consists of these stages:

1. ### `Create API with FastAPI`
   - app = FastAPI()
```bash
uvicorn main:app --host 0.0.0.0 --port 8080
```
2. ### `Build docker image locally`
```bash
docker build -t <image_name> . 
docker run -d -p 8080:8080 --name <container_name > <image_name>
```
3. ### `Docker compose locally`
   * requirements : docker-compose.yaml file
```bash
docker compose up --build 
```
4. ### `Testing built APIS`
   - access this url:  http://0.0.0.0:8080/docs to use FastAPI Swagger to test the API

5. ### `Deploy API via remote server`
   - access the remote server via **ssh** command
   - install docker as guided from [Docker](https://docs.docker.com/engine/install/ubuntu/), for ubuntu.
   - clone this github repo to the remote server, cd into CS317 folder
```bash
docker compose up --build 
```

6. ### `Access API externally`
   - Currently the docker is running locally and can only be accessed via **http://<SERVER_IP>:8080/docs**, and that machine will also have to maintain connect to OpenVPN.
   - [Docker](https://ngrok.com/), will help forward to internet (for demonstration and limit usage only, do not use NGROK for important APIs without protection)
   - you can get the url from ngrok website, by signing for it.
```bash
ngrok http 8080 --url https://example.ngrok.app
```

7. ### `end`
   - Use APIS locally (development environment and quick tests with **Docker, Docker-compose**)
   - Use APIS externally, online (production environment, remote server environment with **Docker, Docker-compose**)

---

## 🚰 Technologies

| Tool/Library | Purpose                                                                                                                                |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------|
| **FastAPI**  | FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.         |
| **Docker**   | Docker helps developers build, share, run, and verify applications anywhere — without tedious environment configuration or management. |
| **ngrok**    | Flexible API gateway for instant, secure connectivity anywhere—public or private.                                                      |


---
## Results
[Serving API and Docker locally](https://youtu.be/ldGWFFqCT4s)

[Serving API and Docker on remote server](https://youtu.be/pX-mLY8qgQs)


[Click me to test api](https://noble-coyote-measured.ngrok-free.app/docs#/default/evaluate_evaluate_post)

## 📬 Contact

For questions, feedback, or contributions, feel free to open an issue or contact via GitHub.
