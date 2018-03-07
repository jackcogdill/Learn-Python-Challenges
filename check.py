#! /usr/bin/env python

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
    '03': { '0': 'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e',
            '1': '7846cdd4c2b9052768b8901640122e5282e0b833a6a58312a7763472d448ee23781c7f08d90793fdfe71ffe74238cf6e4aa778cc9bb8cec03ea7268d4893a502',
            '2': '501e8b05a3c74a8c54f22ae978dfd52aaac23f876af7f30b67caa65b5c58a628596d8888933fed67c283907b81863307fd48dadbceefe3980e866064655d6d77',
            '3': '13be82730e2c5d9937b51b878fa279c020ca513a3f5c24079a3cb1fef46c23c899317a5f6778ccd9ce55ebb91fbb2482970bd37edf0d6f845121ad57da1e57d1',
            '4': '7f308714acd9da3b39850c7978875d3f31cd440f0506fa4a4e615d53510e40aa508975134bfea0597c31098b380b8a4098440c13ff78ec51791c2b2201877fb6',
            '5': 'b662d4bfd45d2006cbfd3af5aa71e3edd1842a61bfd6185b9a5799970ce595507171f2b82dde570197b1941a9a846ab167830f0b542c8cb9ffd9e462aeccf6a3',
            '6': 'ff44491145ebb2b9a6a9002fe6229ef860bee455c2d6c12c2a68bbebb1b5f2150031ba720d058ad5480eb620879eb704b3621ed412c9d5a618a9b2a580a80c3f',
            '7': 'bc1dbb963c54dce0dcb7313f734b2db647d4a3bdda467a10d29756e3125e6b7f15b966bb9cc4401d0535e800c78f165a30cc37f5e4515317464bf94d27133beb',
            '8': 'b7243a70f6b934725f35428d58d849154b310996d5b1a49e7e6bd85ab3e00f96ee1403f1fceec7fcf84f1e20bb904367568ac484a5694f14532f9c66c3787d18',
            '9': '9e39043c2c5aa1da2829b1fc30efda72ae22e8c76b69b39989ac818ffc0c0f32e4df9b4a3a83185268424e5e288e02fc0f0aed7add3561d23889a19b7b758f1b'},
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
            output = run(['python', file], case)
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
        output = run(['python', file])
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
            output = run(['python', file], testcase)
            answer = sha512(output.strip())
            answers[testcase] = answer

        import pprint
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(answers)
    else: # Normally check program
        file = args[1]
        check(file)

