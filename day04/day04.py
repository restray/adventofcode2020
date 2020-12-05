def listContains(src, compare):
    i = 0
    for c in compare:
        if c in src:
            i += 1
    return i == len(compare)

def part01(fields):
    passports = fields.split('\n\n')
    passportCount = 0
    requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for passport in passports:
        passportFieldList = []
        passportValues = passport.replace('\n', ' ').replace('\r', '').split(' ')
        for passportValue in passportValues:
            PassportKey, PassportValue = passportValue.split(":")
            passportFieldList.append(PassportKey)
        if listContains(passportFieldList, requiredFields):
            passportCount += 1
    return passportCount

def checkHeight(value):
    if value[len(value) - 2:] == 'cm' and int(value[:len(value) - 2]) >= 150 and int(value[:len(value) - 2]) <= 193:
        return True
    elif value[len(value) - 2:] == 'in' and int(value[:len(value) - 2]) >= 59 and int(value[:len(value) - 2]) <= 76:
        return True
    return False

def checkHairColor(value):
    validator = "abcdef0123456789"
    if len(value) == 7 and value[0] == '#':
        for c in value[1:]:
            if c not in validator:
                return False
        return True
    return False

def checkPassportValidation(fields):
    valid = True
    for field, value in fields.items():
        if field == 'byr':
            if not (value.isdigit() and int(value) >= 1920 and int(value) <= 2002):
                return False
        elif field == 'iyr':
            if not (value.isdigit() and int(value) >= 2010 and int(value) <= 2020):
                return False
        elif field == 'eyr':
            if not (value.isdigit() and int(value) >= 2020 and int(value) <= 2030):
                return False
        elif field == 'hgt':
            if not (checkHeight(value)):
                return False
        elif field == 'hcl':
            if not (checkHairColor(value)):
                return False
        elif field == 'ecl':
            if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return False
        elif field == 'pid':
            if not (len(value) == 9 and value.isdigit()):
                return False
    return True

def part02(fields):
    passports = fields.split('\n\n')
    passportCount = 0
    requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for passport in passports:
        passportKeyList = []
        passportFieldList = {}
        passportValues = passport.replace('\n', ' ').replace('\r', '').split(' ')
        for passportValue in passportValues:
            PassportKey, PassportValue = passportValue.split(":")
            passportKeyList.append(PassportKey)
            passportFieldList[PassportKey] = PassportValue
        if listContains(passportKeyList, requiredFields) and checkPassportValidation(passportFieldList):
            passportCount += 1
    return passportCount

if __name__ == "__main__":
    with open('input.txt', 'r') as fields:
        # print(part01(fields.read()))
        print(part02(fields.read()))