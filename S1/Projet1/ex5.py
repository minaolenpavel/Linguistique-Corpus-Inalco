class SegmentationResult:
    def __init__(self, segmentation:tuple) -> None:
        self.token1:str = segmentation[0]
        self.token1Map:str = segmentation[1]
        self.token2:str = segmentation[2]
        self.token2Map:str = segmentation[3]
        self.isCorrect:bool = True if self.token1 == self.token2 and self.token1Map == self.token2Map else False

segmentationResults:list = []
with open("results.txt", encoding="utf-8", mode="r") as results:
    for result in results:
        split_result = result.strip().split(";")
        segmentationResult = SegmentationResult(tuple(map(str.strip, split_result)))
        segmentationResults.append(segmentationResult)
    results.close()

total_len = len(segmentationResults)
correct_results_len = len([obj for obj in segmentationResults if obj.isCorrect == True])
incorrect_results_len = len([obj for obj in segmentationResults if obj.isCorrect == False])
print(f"{round((correct_results_len/total_len)*100, 2)}% des mots ont été préservés")