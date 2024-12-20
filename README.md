Markdown

# Turkish-English Translation API with TDK Integration

Bu proje, Türk Dil Kurumu'ndan (TDK) bir kelime çeken, Google Çeviri kullanarak İngilizce'ye çeviren ve hem Türkçe kelimeyi hem de İngilizce çevirisini döndüren basit bir API'dir.

## Özellikler

*   TDK API'sinden "Bir Kelime" başlığı altından bir kelime çeker.
*   Kelimeyi Türkçeden İngilizceye çevirir.
*   API dokümantasyonu için Swagger UI sağlar.

## Gereksinimler

Bu projeyi yerel makinenizde çalıştırmak için şunlara ihtiyacınız olacak:

*   Python 3.6+
*   `pip` (Python paket yöneticisi)

## Kurulum

**1. Depoyu klonlayın**

Terminalinizi veya komut isteminizi açın ve depoyu yerel makinenize klonlamak için aşağıdaki komutu çalıştırın:

```bash
git clone [https://github.com/your-username/turkish-english-translation-api.git](https://github.com/your-username/turkish-english-translation-api.git)
2. Sanal bir ortam oluşturun ve etkinleştirin (isteğe bağlı ancak önerilir)

Proje bağımlılıklarını yönetmek için sanal bir ortam kullanmak iyi bir uygulamadır. İşte nasıl oluşturulacağı ve etkinleştirileceği:

macOS/Linux'ta:

Bash

python -m venv venv
source venv/bin/activate
Windows'ta:

Bash

python -m venv venv
venv\Scripts\activate
3. Bağımlılıkları yükleyin

Gerekli bağımlılıkları pip kullanarak yükleyin:

Bash

pip install -r requirements.txt
Bir requirements.txt dosyanız yoksa, gerekli paketleri manuel olarak yükleyebilirsiniz:

Bash

pip install flask flask-restx requests deep-translator
4. Uygulamayı çalıştırın

Bağımlılıklar yüklendikten sonra, uygulamayı aşağıdaki komutu kullanarak çalıştırabilirsiniz:

Bash

python app.py
5. Swagger UI'ye erişin

Uygulama çalıştıktan sonra, API'yi test etmek ve dokümantasyonu görüntülemek için şu adresten Swagger UI'ye erişebilirsiniz:

http://localhost:5000/swagger/
6. API'yi test etme

/translate uç noktasını test etmek için Swagger UI'yi kullanabilir veya basitçe şu adrese bir GET isteği gönderebilirsiniz:

http://localhost:5000/translate
Yanıt, TDK'dan çekilen rastgele bir Türkçe kelimeyi ve İngilizce çevirisini içerecektir.
