# Problem Set 2, insan_asmaca.py
# İsim: Hünkar Genç
# Katkıda bulunanlar: Grup4
# Harcanan Zaman: 4 Saat

# İnsan Asmaca Oyunu
# -----------------------------------
# Yardımcı kod
# Bu yardımcı kodu anlamanıza gerek yok,
# fakat fonksiyonları nası kullanacağınız bilmeniz
# gerekiyor.
# (öğrenmek için fonksiyon dizelerini okuyun!)
import random
import string
import pandas as pd

KELIME_LISTESI_DOSYASI = "tdk_sozcukler2.csv"
TÜRKÇE_ALFABE = 'abcçdefgğhıijklmnoöprsştuüvyz'

def kelimeleri_yükle():
    """
    Geçerli kelimelerin bir listesini döndürür. 
    Kelimeler, küçük harflerden oluşan dizelerdir.
    
    Sözcük listesinin boyutuna bağlı olarak, bu işlevin 
    tamamlanması biraz zaman alabilir.
    """
    print("Dosyadan kelime listesi okunuyor...")
    # dosyanın okunması
    dosya = pd.read_csv("tdk_sozcukler2.csv")
    # sözcüklerin küçük harfe çevrilmesi
    dosya['SOZCUKLER'] = dosya['SOZCUKLER'].str.lower() 
    # wordlist: list of strings
    kelime_listesi = dosya['SOZCUKLER'].tolist()
    print(f"{len(kelime_listesi)} kelimelik liste hazırlandı.")
    return kelime_listesi


def kelime_seç(kelime_listesi):
    """
    kelime_listesi (liste): kelimelerin listesi (dize)
    
    Kelime listesinde rastgele bir keliem döndürür.
    """
    return random.choice(kelime_listesi)

# yardımcı kodların sonu

# -----------------------------------

# Programın herhangi bir yerinden erişilebilmesi için kelime 
# listesini değişken kelime_listesine yükleyin
kelime_listesi = kelimeleri_yükle()


def kelime_tahmin_edildi_mi(gizli_kelime, tahmin_edilen_harfler):
    '''
    gizli_kelime: dize, kullanıcının tahmin ettiği kelime; 
        tüm harflerin küçük olduğunu varsayar
    tahmin_edilen_harfler: şimdiye kadar tahmin edilen harflerin listesi; 
        tüm harflerin küçük olduğunu varsayar
    döndürdüğü: boolean, gizli_kelime'nin tüm harfleri tahmin_edilen_harfler içindeyse True; 
        aksi takdirde False
    '''
    # KODUNUZU BURAYA YAZIN VE "pass" İFADESİNİ SİLİN
    for x in gizli_kelime:
        if x not in tahmin_edilen_harfler:
            return False
    return True
    #pass



def tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler):
    '''
    gizli_kelime: dize, kullanıcının tahmin ettiği kelime; 
        tüm harflerin küçük olduğunu varsayar
    tahmin_edilen_harfler: şimdiye kadar tahmin edilen harflerin listesi; 
        tüm harflerin küçük olduğunu varsayar
    döndürdüğü: dize, harflerden oluşur, alt çizgiler (_) ve gizli_kelime içindeki hangi harflerin 
        şimdiye kadar tahmin edildiğini temsil eden boşluklardan oluşur.
    '''
    # KODUNUZU BURAYA YAZIN VE "pass" İFADESİNİ SİLİN
    guessedWord=['_']*len(gizli_kelime)
    for x in tahmin_edilen_harfler :
        occurences = []
        for i, j in enumerate(gizli_kelime):
             if j == x:
                occurences.append(i)
        for i in occurences :
            guessedWord[i]=x
    return ''.join(guessedWord)
    # pass



def uygun_harfleri_al(tahmin_edilen_harfler, alfabe = TÜRKÇE_ALFABE):
    '''
    tahmin_edilen_harfler: şimdiye kadar tahmin edilen harflerin listesi; 
        tüm harflerin küçük olduğunu varsayar
    döndürdüğü: dize (harfler), Henüz tahmin edilmemiş harfleri temsil 
        eden harflerden oluşur.
    '''
    # alfabedeki harfleri alır
    alfabe = TÜRKÇE_ALFABE
    available_Letters=[]
    # KODUNUZU BURAYA YAZIN VE "pass" İFADESİNİ SİLİN
    for x in alfabe :
         if (x not in tahmin_edilen_harfler):
             available_Letters.append(x)
    return ''.join(available_Letters)

    #pass
    
    

def insan_asmaca(gizli_kelime, alfabe = TÜRKÇE_ALFABE):
    '''
    gizli_kelime: dize, kullanıcının tahmin ettiği kelime; 
        tüm harflerin küçük olduğunu varsayar

    Etkileşimli bir İnsan Asmaca oyunu başlatır.
    
     * Oyunun başında kullanıcıya gizli_kelime'nin kaç harf içerdiğini 
       ve kaç tahminle başladığını bildirin.
      
     * Kullanıcı 6 tahminle başlamalıdır

     * Her turdan önce kullanıcıya kaç tahmin yaptğını ve henüz tahmin 
       etmediği harfleri göstermelisiniz.
    
     * Kullanıcıdan tur başına bir tahmin yapmasını isteyin. Kullanıcının 
       bir harf yazdığından emin olmayı unutmayın!
    
     * Kullanıcı, tahminlerinin bilgisayarın kelimesinde görünüp görünmediğine 
       dair her tahminden hemen sonra geri bildirim almalıdır.

     * Her tahminden sonra, kullanıcıya o ana kadar kısmen tahmin edilen 
       kelimeyi göstermelisiniz.
    
    Problem yönergesinde detaylandırılan diğer sınırlamaları takip edin.
    '''
    # alfabedeki harfleri alır
    alfabe = TÜRKÇE_ALFABE
    # KODUNUZU BURAYA YAZIN VE "pass" İFADESİNİ SİLİN
    intro = str(len(gizli_kelime))
    tahmin_edilen_harfler = []
    guess = str
    mistakesMade = 6
    wordGuessed = False
    
    print('İnsan Asmaca oyununa hoşgeldiniz!')
    print(intro + (' harfli bir kelime düşünüyorum.'))
    print('------------')

    while mistakesMade > 0 and mistakesMade <= 6 and wordGuessed is False:
        if gizli_kelime == tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler):
            wordGuessed = True
            break
        print(str(mistakesMade) + (' tahmin hakkınız kaldı.'))
        print('Uygun harfler: ', uygun_harfleri_al(tahmin_edilen_harfler))
        guess = input('Lütfen bir harf tahmin et: ').lower()
        if guess in gizli_kelime:
            if guess in tahmin_edilen_harfler:
                print("Oops! O mektubu zaten tahmin ettin: ",tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler))
                print('------------')
            else:
                tahmin_edilen_harfler.append(guess)
                print('Güzel tahmin: ',tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler))
                print('------------')
        else:
            if guess in tahmin_edilen_harfler:
                print("Oops! O harfi zaten tahmin ettin: ", tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler))
                print('------------')
            else:
                tahmin_edilen_harfler.append(guess)
                mistakesMade -= 1
                print('Oops! O harf benim kelimemde değil: ',tahmin_edilen_kelimeyi_al(gizli_kelime,tahmin_edilen_harfler))
                print('------------')

    if wordGuessed == True:
        return 'Tebrikler kazandın!'
    elif mistakesMade == 0:
        print('Üzgünüm, tahmininiz bitti. Kelime ', gizli_kelime) 
    # pass



# insan_asmaca fonksiyonunuzu tamamladıktan sonra bu dosyanın en altına inin
# ve kodunuzu test etmek için ilk iki yorum satırının yorum işaretlerini kaldırın.
# (ipucu: kendi testinizi yaparken kendi gizli_kelimenizi'ünüzü seçmek 
# isteyebilirsiniz)


# -----------------------------------



def boşluklarla_eşleştir(benim_kelimem, diğer_kelime):
    '''
    benim_kelimem: _ karakterli dize, geçerli gizli_kelime tahmini
    diğer_kelime: dize, normal Türkçe kelime
    döndürdüğü: boolean, eğer benim_kelimem'in tüm gerçek harfleri 
       diğer_kelime'nin karşılık gelen harfleriyle eşleşiyorsa veya 
       harf özel sembol _ ise ve benim_kelimem ve diğer_kelim aynı 
       uzunluktaysa True; aksi takdirde False. 
    '''
    # KODUNUZU BURAYA YAZIN VE "pass" İFADESİNİ SİLİN
    len_my_word = len(benim_kelimem.replace(" ", ""))
    len_other_word = len(diğer_kelime)
    other_list = list(diğer_kelime)
    my_list = list(benim_kelimem.replace(" ", "").replace("_", ""))  

    if bool(my_list) : 
        if len_my_word == len_other_word:
            for w in my_list :
                if my_list.count(w) == other_list.count(w):  
                    if w in other_list : 
                        if [k for k, x in enumerate(list(benim_kelimem.replace(" ", ""))) if x == w] == \
                           [k for k, x in enumerate(other_list) if x == w] :
                            accuracy = True
                            continue
                        else :
                            accuracy = False
                            break
                    else :
                        accuracy = False
                        break
                else :
                    accuracy = False
                    break
    
        else :
            accuracy = False
    else :
        if len_my_word == len_other_word :
            accuracy = True 

    return accuracy
    # pass



def olası_eşleşmeleri_göster(benim_kelimem):
    '''
    benim_kelimem: _ karakterli dize, geçerli gizli_kelime tahmini
    döndürdüğü: hiçbir şey, ancak kelime listesindeki my_word ile eşleşen her kelimeyi 
             yazdırmalıdır. Ekranda bir harf tahmin edildiğinde, o harfin gizli kelimede 
             geçtiği tüm pozisyonların ortaya çıktığını unutmayın. Bu nedenle, 
             gizli harf (_) zaten açığa çıkmış kelimedeki harflerden biri olamaz.
    '''
    # KODUNUZU BURAYA YAZIN VE "pass" İFADESİNİ SİLİN
    hint_list = []

    for word in kelime_listesi:
        # print(word)
        if boşluklarla_eşleştir(benim_kelimem, word) == True :
            hint_list.append(word)        

    return hint_list
    # pass



def ipuçlarıyla_insan_asmaca(gizli_kelime, alfabe=TÜRKÇE_ALFABE):
    '''
    gizli_kelime: dize, kullanıcının tahmin ettiği kelime; 
        tüm harflerin küçük olduğunu varsayar
    
    Etkileşimli bir İnsan Asmaca oyunu başlatır.
    
     * Oyunun başında kullanıcıya gizli_kelime'nin kaç harf içerdiğini 
       ve kaç tahminle başladığını bildirin.
      
     * Kullanıcı 6 tahminle başlamalıdır

     * Her turdan önce kullanıcıya kaç tahmin yaptğını ve henüz tahmin 
       etmediği harfleri göstermelisiniz.
    
     * Kullanıcıdan tur başına bir tahmin yapmasını isteyin. Kullanıcının 
       bir harf yazdığından emin olmayı unutmayın!
    
     * Kullanıcı, tahminlerinin bilgisayarın kelimesinde görünüp görünmediğine 
       dair her tahminden hemen sonra geri bildirim almalıdır.

     * Her tahminden sonra, kullanıcıya o ana kadar kısmen tahmin edilen 
       kelimeyi göstermelisiniz.
     
     * Tahmin, * sembolüyse, kelime listesindeki mevcut tahmin edilen kelimeyle 
       eşleşen tüm kelimeleri yazdırın.
    
    Problem yönergesinde detaylandırılan diğer sınırlamaları takip edin.
    '''
    # alfabedeki harfleri alır
    alfabe = TÜRKÇE_ALFABE
    # KODUNUZU BURAYA YAZIN VE "pass" İFADESİNİ SİLİN
    print('İnsan Asmaca oyununa hoş geldiniz!')
    length_of_letter = len(gizli_kelime)

    print(length_of_letter, 'harfli bir kelime düşünüyorum.' )

    left_num_guesses = 6 
    left_num_worning = 3
    tahmin_edilen_harfler = []
    vowel = ['a', 'i', 'u', 'e', 'o']
    num_of_try = 0
    num_of_secretword = len(gizli_kelime)
    
    print('----------')

    while left_num_guesses > 0:
        print(left_num_guesses, ' tahmin hakkınız kaldı.' )
        print('Uygun harfler:', ''.join(uygun_harfleri_al(tahmin_edilen_harfler)))

        input_letter_all = str(input('Lütfen bir harf tahmin et:'))
        input_letter = input_letter_all.lower()

        available_list = uygun_harfleri_al(tahmin_edilen_harfler)

        if input_letter == '*' :
            if length_of_letter - tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler).count("_") == 0 :
                print("En az bir harf tahmin etmelisiniz!")
                continue
            else :
                print(olası_eşleşmeleri_göster(tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler)))

        elif input_letter in available_list :
            if input_letter in list(gizli_kelime):
                tahmin_edilen_harfler.append(input_letter)
                print('Güzel tahmin: ', tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler))
            else :
                tahmin_edilen_harfler.append(input_letter)
                print('Oops! O harf benim kelimemde değil: ', \
                    tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler))
                if input_letter in vowel :
                    left_num_guesses -= 2
                else :
                    left_num_guesses -= 1

        elif input_letter in tahmin_edilen_harfler :
            tahmin_edilen_harfler.append(input_letter)
            if left_num_worning > 0 :
                left_num_worning -= 1
                print("Oops! O harfi zaten tahmin ettiniz. ", left_num_worning,\
                "hataya sahipsin.:", tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler))
            else :
                left_num_guesses -=1
                print("Oops! O harfi zaten tahmin ettiniz. ", left_num_guesses, \
                "tahmin hakkın kaldı :", tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler))   

        else :
            tahmin_edilen_harfler.append(input_letter)
            if left_num_worning > 0 :
                left_num_worning -= 1
                print('Oops! Bu geçerli bir harf değil. ', left_num_worning, \
                'hataya sahipsin : ', tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler))
            else :
                left_num_guesses -= 1
                print('Oops! Bu geçerli bir harf değil. You have', left_num_guesses, \
                'tahmin hakkın kaldı: ', tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler))

        num_of_try += 1
        
        comparison = len((tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler))) - \
                    (tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler)).count("_") - \
                    (tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler)).count(" ")

        if comparison == num_of_secretword :
            print('Tebrikler, kazandın! ')
            print('Bu oyun için toplam puanınız: ', num_of_try)
            break

        print('----------')
    
    if left_num_guesses == 0 :
        print("Üzgünüm kaybettin!")

    return
    # pass


# ipuçlarıyla_insan_asmaca fonksiyonunu tamamladıktan sonra, yukarıdaki
# insan_asmaca fonksiyonundakine benzer şekilde iki yorum satırının yorum
# işaretlerini kaldırıp dosyayı çalıştırarak kodunuzu test edin.
# ipucu: kendi testinizi yaparken kendi gizli_kelimenizi'ünüzü seçmek 
# isteyebilirsiniz


if __name__ == "__main__":
    # pass

    # Bölüm 2'yi test etmet için, yukarıdaki "pass" satırına yorum işaretini
    # ekleyin ve aşağıdaki iki satırın yorum işaretlerini kaldırın.
    
    # gizli_kelime = kelime_seç(kelime_listesi)
    # insan_asmaca(gizli_kelime, alfabe=TÜRKÇE_ALFABE)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines.
    # Bölüm 3'ü test etmek için yukarıdaki satırlara yeniden yorum işaretlerini
    # ekleyin ve aşağıdaki iki satırın yorum işaretlerini kaldırın.
    
    gizli_kelime = kelime_seç(kelime_listesi)
    ipuçlarıyla_insan_asmaca(gizli_kelime, alfabe=TÜRKÇE_ALFABE)