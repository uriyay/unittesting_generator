#format:
#unittesting = {'module_name' : {
#       'func_name' : [(inputs, output),
#                      (inputs, output)
#                     ],
#       }
#   }
#

unittesting = {
        'something' : {
            'add' : 
                [((1, 2), 3),
                 ((-1, 2), 1),
                 ((-1, -2), -3),
                 ((0, 1), 1),
                 ((0, -1), -1),
                 (('a', 'b'), 'ab')
                 ],
            'sub' : 
                [((1, 2), -1),
                 ((-1, 2), -3),
                 ((-1, -2), 1),
                 ((0, 1), -1),
                 ((0, -1), 1),
                ],
            },
    }
