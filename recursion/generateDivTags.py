def generateDivTags(numberOfTags):
    matchedTags = []
    generateDivTagsFromPrefix(numberOfTags, numberOfTags, "", matchedTags)
    return matchedTags 


def generateDivTagsFromPrefix(openingTagsNeeded, closingTagsNeeded, prefix, result):
    if openingTagsNeeded > 0:
        newPrefix = prefix + "<div>"
        generateDivTagsFromPrefix(openingTagsNeeded - 1, closingTagsNeeded, newPrefix, result)

    if openingTagsNeeded < closingTagsNeeded:
        newPrefix = prefix + "</div>"
        generateDivTagsFromPrefix(openingTagsNeeded, closingTagsNeeded - 1, newPrefix, result)

    if closingTagsNeeded == 0:
        result.append(prefix)


if __name__ == '__main__':
    print(generateDivTags(3))