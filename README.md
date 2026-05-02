# Docker-Ansible-CICD-Demo

## 1. Proje Adı
Docker, Ansible ve GitHub Actions ile Uçtan Uca CI/CD Pipeline ve Web Uygulaması Dağıtımı

## 2. Proje Amacı
Bu proje, modern DevOps pratiklerini uygulamalı olarak göstermek amacıyla geliştirilmiştir. Temel amaç, Python Flask ile yazılmış basit bir web uygulamasını Docker ile containerize etmek, GitHub Actions kullanarak CI/CD süreçlerini otomatize etmek ve Ansible aracıyla uzak bir sunucuya kesintisiz deploy etmektir. 

## 3. Kullanılan Teknolojiler
- **Uygulama Geliştirme:** Python 3.10, Flask
- **Containerization (Konteynerleştirme):** Docker, Docker Hub
- **CI/CD (Sürekli Entegrasyon & Teslimat):** GitHub Actions
- **Configuration Management (Yapılandırma Yönetimi):** Ansible
- **Sunucu İşletim Sistemi:** Ubuntu Linux

## 4. Genel Mimari Akış
1. Geliştirici kodu yazar ve GitHub'daki `main` branch'ine push yapar.
2. GitHub Actions tetiklenir ve pipeline çalışmaya başlar.
3. Uygulamanın Docker imajı (Python 3.10 slim tabanlı) build edilir.
4. Oluşturulan bu imaj Docker Hub'a gönderilir (push).
5. GitHub Actions runner'ı üzerinde Ansible kurulur ve gerekli kimlik doğrulamaları (SSH) yapılır.
6. Ansible, hedef Ubuntu sunucusuna bağlanarak eski container'ı durdurur, siler ve yeni imajı pull ederek yeni container'ı 80 portu üzerinden dışarıya açarak çalıştırır.

## 5. Klasör Yapısı
```text
docker-ansible-cicd-demo/
├── .github/
│   └── workflows/
│       └── ci-cd.yml      # CI/CD otomasyon adımlarını içeren pipeline dosyası
├── ansible/
│   ├── deploy.yml         # Hedef sunucuya deploy yapacak Ansible playbook'u
│   └── inventory.ini      # Ansible için hedef sunucu IP ve erişim bilgileri
├── app/
│   ├── app.py             # Flask web uygulaması ana kod dosyası
│   └── requirements.txt   # Python bağımlılıkları (Flask, vb.)
├── .gitignore             # Git versiyon kontrolünden dışlanacak dosyalar
├── Dockerfile             # Uygulamanın Docker imajını oluşturma talimatları
└── README.md              # Proje dokümantasyonu (bu dosya)
```

## 6. Local (Yerel) Çalıştırma Adımları
Projeyi bilgisayarınızda sadece Python kullanarak çalıştırmak isterseniz:
1. Terminali açın ve `app` dizinine gidin: `cd app`
2. Bağımlılıkları yükleyin: `pip install -r requirements.txt`
3. Uygulamayı başlatın: `python app.py`
4. Tarayıcınızdan `http://localhost:5000` adresine giderek uygulamayı görüntüleyin.

## 7. Docker Build ve Run Komutları
Projeyi yerel makinenizde Docker üzerinde test etmek isterseniz projenin ana dizininde (Dockerfile'ın bulunduğu yerde) sırasıyla şu komutları çalıştırın:
```bash
# Docker imajını derleme
docker build -t cicd-demo-app .

# İmajı container olarak çalıştırma (Hostun 5000 portunu containerın 5000 portuna bağlar)
docker run -d -p 5000:5000 --name cicd-demo-test cicd-demo-app
```
Çalıştığından emin olmak için tarayıcınızda `http://localhost:5000` adresine gidin. İşiniz bittiğinde container'ı `docker stop cicd-demo-test` ve `docker rm cicd-demo-test` komutlarıyla silebilirsiniz.

## 8. GitHub Secrets Açıklaması
GitHub Actions'ın Docker Hub'a ve hedef Ubuntu sunucusuna güvenli bir şekilde bağlanabilmesi için deponuzun **Settings > Secrets and variables > Actions** kısmından aşağıdaki değişkenlerin tanımlanması zorunludur:
- `DOCKER_USER`: Docker Hub kullanıcı adınız.
- `DOCKER_PASS`: Docker Hub şifreniz veya Personal Access Token (önerilir).
- `SERVER_IP`: Ansible'ın bağlanıp deploy yapacağı uzak sunucunun Public IP adresi.
- `SSH_KEY`: Uzak sunucuya bağlantı kurarken kullanılacak olan SSH private key'i (örn. `id_rsa` içeriği).

## 9. CI/CD Pipeline Açıklaması
Pipeline, `.github/workflows/ci-cd.yml` dosyası üzerinden yönetilir. Pipeline'ın temel adımları:
- **Build ve Push:** Projedeki değişiklikler yakalanır, Docker imajı baştan oluşturulur ve Docker Hub üzerine `DOCKER_USER/myapp:latest` etiketiyle yüklenir.
- **Sed Değişimleri:** `inventory.ini` ve `deploy.yml` içindeki `YOUR_SERVER_IP` ve `Suwde` gibi geçici metinler, pipeline çalışma anında gerçek "Secrets" değerleriyle otomatik olarak değiştirilir.
- **Güvenlik Ayarları:** Uzak sunucu ile bağlantı kurmak için SSH anahtarları oluşturulur ve `known_hosts` dosyası güncellenir.

## 10. Ansible Deploy Süreci
GitHub Actions üzerinden tetiklenen `ansible/deploy.yml` playbook'u hedef makinede sırasıyla şunları yapar:
1. `docker.io` paketi kurulu değilse yükler.
2. Docker servisinin arka planda çalışır ve aktif (enabled) olduğundan emin olur.
3. Daha önce çalışan `myapp` adında bir container varsa bunu durdurur ve siler (İdempotency).
4. Docker Hub'dan uygulamanın en güncel (`latest`) imajını çeker.
5. Yeni container'ı başlatır ve dışarıdan `80` portu (HTTP) üzerinden erişime açar.

## 11. Ekran Görüntüleri
Aşağıdaki alana projeyi çalıştırdıktan sonra alınan ekran görüntüleri eklenebilir:

![Uygulama Ekran Görüntüsü](placeholder_image_link_here)
*(Buraya canlı sunucudaki veya yerel ortamdaki uygulamanın ekran görüntüsünü yerleştiriniz)*

![GitHub Actions Başarılı Pipeline](placeholder_actions_link_here)
*(Buraya GitHub Actions'ın başarılı şekilde tamamlandığını gösteren ekran görüntüsünü yerleştiriniz)*

## 12. Sonuç
Bu proje, yazılımın geliştirme aşamasından sunucuya otomatik olarak dağıtılmasına (deploy) kadar geçen DevOps süreçlerinin temel prensiplerini göstermektedir. Konteyner teknolojisi sayesinde "benim bilgisayarımda çalışıyordu" problemi ortadan kaldırılmış; Ansible ve CI/CD pratikleriyle manuel süreçler otonom hale getirilerek insan hatası payı en aza indirilmiştir.
