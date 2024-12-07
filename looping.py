student_scores = {
    'Wahyu': [90, 85, 80],
    'Rofiq': [70, 75, 80],
    'Faisal': [80, 85, 90],
    'Yahya': [90, 95, 100],
    'Dyah': [95, 90, 85]
}

def check_nilai(data):
    nilai = []
    for k,v in data.items():
        rata_rata = 0
        banyak_nilai = 0
        for i in v:
            rata_rata += i
            banyak_nilai += 1
        nilai.append({f'{k}': rata_rata/banyak_nilai})

    for i in nilai:
        for k,v in i.items():
            if v > 85:
                print(f'{k} mendapatkan nilai A')
            elif v > 75:
                print(f'{k} mendapatkan nilai B')
            elif v > 65:
                print(f'{k} mendapatkan nilai C')
            else:
                print(f'{k} mendapatkan nilai D')

check_nilai(student_scores)


def info_kelas(data):
    rata_rata = []
    for k,v in data.items():
        rata_rata.append({f'{k}': sum(v)/len(v)})

    for i in rata_rata:
        for k,v in i.items():
            if v > 85:
                print(f'{k} mendapatkan nilai A')
            elif v > 75:
                print(f'{k} mendapatkan nilai B')
            elif v > 65:
                print(f'{k} mendapatkan nilai C')
            else:
                print(f'{k} mendapatkan nilai D')
        
    minimal = min([min(v) for v in data.values()])
    maksimal = max([max(v) for v in data.values()])

    # print(f'Nilai terendah dalam kelas ini adalah {minimal}')
    # print(f'Nilai tertinggi dalam kelas ini adalah {maksimal}')

    # print(rata_rata)
    top_performer = []
    for i in rata_rata:
        for k,v in i.items():
            if v > 85:
                top_performer.append(f'{k} mendapatkan nilai A')
    
    print(top_performer)

    # print(rata_rata)

info_kelas(student_scores)
