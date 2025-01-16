def pattern_accuracy(pattern:str, ref_pattern:str) -> float:
    total_annotations = len(ref_pattern)
    correct = 0
    precision = 0
    if len(pattern) == total_annotations:
        for i, value in enumerate(pattern):
            if value == ref_pattern[i]:
                correct+=1
        precision = (correct/total_annotations)*100
    
    return precision

def pattern_absolute_accuracy(pattern:str, ref_pattern:str) -> int:
    if pattern == ref_pattern:
        return 1
    else:
        return 0

def import_corpus(path:str) -> list:
    corpus = []
    with open(path, "r", encoding='utf-8') as file:
        for line in file:
            corpus.append(line.strip().split(" "))
    return corpus

def calculate_avg_accuracy(ref_corpus:list, corpus:list) -> float:
    all_precision = []
    for i, value in enumerate(corpus):
        accuracy = pattern_accuracy(value[1], ref_corpus[i][1])
        all_precision.append(accuracy)

    total = len(all_precision)
    avg = sum(all_precision)/total
    return avg

def calculate_category_accuracy(ref_corpus:list, corpus:list) -> float:
    all_precision = []
    for i, value in enumerate(corpus):
        accuracy = pattern_accuracy(value[1][0], ref_corpus[i][1][0])
        all_precision.append(accuracy)
    
    total = len(all_precision)
    avg = sum(all_precision)/total
    return avg

def calculate_pattern_accuracy_per_category(ref_corpus:list, corpus:list) -> dict:
    correct_per_cat = {}
    for i, value in enumerate(corpus):
        ref_pattern = ref_corpus[i][1]
        accuracy = pattern_accuracy(value[1], ref_pattern)
        if ref_pattern[0] in correct_per_cat.keys():
            correct_per_cat[ref_pattern[0]].append(accuracy)
        else:
            correct_per_cat[ref_pattern[0]] = [accuracy]
    
    accuracy_per_category = {}
    for key in correct_per_cat.keys():
        accuracy_per_category[key] = (sum(correct_per_cat[key])/len(correct_per_cat[key]))
    return accuracy_per_category

def calculate_absolute_accuracy(ref_corpus:list, corpus:list) -> float:
    all_results = []
    for i, value in enumerate(corpus):
        result = pattern_absolute_accuracy(value[1], ref_corpus[i][1])
        all_results.append(result)
    
    total = len(all_results)
    avg = (sum(all_results)/total)*100

    return avg

if __name__ == "__main__":
    ref_corpus = import_corpus("DDHC_REF.txt")
    corpus = import_corpus("DDHC_B.txt")
    avg_accuracy = calculate_avg_accuracy(ref_corpus, corpus)
    print(f"Précision moyenne par mot = {avg_accuracy:.4}%")
    category_accuracy = calculate_category_accuracy(ref_corpus, corpus)
    print(f"Précision des catégories grammaticales = {category_accuracy:.4}%")

    accuracy_per_category = calculate_pattern_accuracy_per_category(ref_corpus, corpus)
    for key, value in accuracy_per_category.items():
        print(f"Les {key} ont une précision de {value:.4}%")

    absolute_accuracy = calculate_absolute_accuracy(ref_corpus, corpus)
    print(f"Précision absolue (Y/N) = {absolute_accuracy:.4}%")

