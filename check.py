#! /usr/bin/env python3

import hashlib
import subprocess
import sys

testcases = {
    '01': '9f71f98eec1ba526da6db07923748b2636838c90ce8fc54497894dac79e3ccd0e0fedcbc5e918c994552a87c8f7ae78b3c0efe4f21d227d843fab1d69e63f5f1',
    '02': { '0': 'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e',
            '1': '7846cdd4c2b9052768b8901640122e5282e0b833a6a58312a7763472d448ee23781c7f08d90793fdfe71ffe74238cf6e4aa778cc9bb8cec03ea7268d4893a502',
            '2': 'd26acb2086c8cf35a09b7f60fbe1eb6584af73a9094bc7348958b9d0bebb8e27ac40be26653fc1c3458d7b66e01bcc06aa430f2e1a49ed9849bc64478c025915',
            '3': 'aa44c21ee3f871e3dfb65f163e27f339ed53b09cb6506776e4164d8844a80700ef43229640e28f947df1c1b4977ca877d69bc3f9eb5129f062bf6304976922a1',
            '4': '4c39792421e6b3df621eb3b940cb3fc7a8c929f639c437735eae491d6062d7b5e475d15af25e38800694f842befcceaf9dd494bc054a8338d0a8cda173b1ca1a',
            '5': '285e7c67957cb8679b068f7a94b9439fae209afbfb4c89f59371fee36a6a458f18e51ef7c9df2d5b81d6545a78f469f87cab854241c0d79f18b79209f69d8a06',
            '6': '77e3e75c06e8e52b409f0616db50d8608e7f201e7019d706ee5c9bc1899f61a9814fb08261b40b83d407ab9a52edcbaf5b6a6a47cade262b119ad263c7589903',
            '7': 'bee55b4b258c942f3c8d7e9e959cdc044cde136f5fc4904b7ab8c357e5a6aa5caff278d278a0da3013afd546287b900001dad23a09d0cd1ae2a85844faeab503',
            '8': '77961e3b047dc0e569a28e4a960dd0655dd09c8019a4c96fa475fac923fa8aa533844c04694b2cb70608ebc658c407dd3586d1430f043c0b5f361a59821e4368',
            '9': '350b2bcb3fa76e3bd60847b91773d9b413202b8a56174ecc7740b795ab476edb5198dd7c26644a66337805a8d95f2e37a091f6467758e1251ebe305092fdd3c9'},
}

def sha512(string):
    string = string.encode('utf-8')
    return hashlib.sha512(string).hexdigest()

def fatal(message):
    print(message)
    exit(1)

def run(command, Input=None):
    process = subprocess.run(command, stdout=subprocess.PIPE, input=Input, encoding='utf-8')
    return process.stdout

def check(file):
    challenge = file.replace('.py', '')
    if challenge not in testcases:
        fatal('Challenge number not found / not supported yet.')

    happy = '\(・ᴗ・)/'
    sad = '(_ _)'

    cases = testcases[challenge]
    if isinstance(cases, dict): # Multiple inputs
        for case, expected in cases.items():
            output = run(['python3', file], case)
            actual = sha512(output.strip())

            if actual != expected:
                print('Failing testcase with input: "%s"' % case)
                print('Your output:')
                print(output)
                print('Sorry, keep trying.  ' + sad)
                break
        else:
            print('All answers correct, way to go!  ' + happy)
    else: # Single (no input)
        output = run(['python3', file])
        print('Your output:')
        print(output)

        expected = testcases[challenge]
        actual = sha512(output.strip())

        if actual == expected: # Correct
            print('Correct answer, way to go!  ' + happy)
        else: # Incorrect
            print('Sorry, wrong answer.  ' + sad)

if __name__ == '__main__':
    args = sys.argv
    argc = len(args)
    def verify(Min, usage):
        if argc < Min:
            fatal(usage)

    verify(2, 'Usage: %s FILE' % args[0])

    if args[1] in ['-g', '--generate']: # Generate test case answers
        verify(4, 'Usage: %s %s FILE TESTCASES' % (args[0], args[1]))

        file = args[2]
        answers = {}
        for i in range(3, argc):
            testcase = args[i]
            output = run(['python3', file], testcase)
            answer = sha512(output.strip())
            answers[testcase] = answer

        import pprint
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(answers)
    else: # Normally check program
        file = args[1]
        check(file)

