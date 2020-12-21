import regex as re

def parse(raw):
    rules, words = data.split('\n\n')
    rules = rules.split('\n')
    words = words.split('\n')
    rules_dict = {}
    for rule in rules:
        rule = rule.split(': ')
        rules_dict[rule[0]] = rule[1].split(' ')
        if rule[1][0] == '"':
            rules_dict[rule[0]] = str(rule[1][1])
    return rules_dict, words


def get_rule(id, rules):
    if(id == '|'):
        return ('|')
    rules[id] = rules[id] if isinstance(
        rules[id], str) else "("+"".join(get_rule(new_id, rules) for new_id in rules[id]) + ")"
    return rules[id]


if __name__ == '__main__':
    with open('input') as f:
        data = f.read()
    rules, words = parse(data)
    reg_word = re.compile(get_rule('0', rules))
    print(get_rule('0', rules))
    result = 0
    for line in words:
        if(reg_word.fullmatch(line)):
            result += 1
    print(result)
