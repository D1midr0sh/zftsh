text = 'Мистер и миссис Дурсль проживали в доме номер четыре по Тисовой улице и всегда с гордостью заявляли, что они, ' \
       'слава богу, абсолютно нормальные люди. Уж от кого-кого, а от них никак нельзя было ожидать, чтобы они попали ' \
       'в какую-нибудь странную или загадочную ситуацию'
a = text.split()
aa = [a[i:i + 4] for i in range(0, len(a), 4)]
for i in aa:
    print(*i, sep='\t')