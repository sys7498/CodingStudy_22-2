def solution(phone_book):
    
    hash_map = {} 
    for number in phone_book: 
        hash_map[number] = 1
    print(hash_map)
    
    for number in phone_book:
        jubdooou = '' #접두어
        for num_cut in number:
            jubdooou += num_cut
            if jubdooou in hash_map and jubdooou != number: #기존번호와 같은 경우 제외
                return False
            
    return True