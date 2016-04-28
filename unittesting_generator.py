import sys
import imp

def get_unittesting_script(config):
    output = ''
    imports = 'import unittest\n'
    run_tests_part1 = 'def main():\n'
    run_tests_part2 = '''if __name__ == '__main__':
    main()
    '''
    for module_name, module_config in config.unittesting.iteritems():
        imports += 'import %s\n' % (module_name,)
        output += '\nclass %s_TestCase(unittest.TestCase):\n' % (module_name,)
        for func_name, func_io in module_config.iteritems():
            test_name = 'test_%s_%s' % (module_name, func_name)
            output += '    def %s(self):\n' % (test_name,)
            for func_input, func_output in func_io:
                output += '        self.assertEqual(%s.%s(*%r), %r)\n' % (module_name, func_name, func_input, func_output)
            output += '\n'
            # run_tests_part1 += '    %s()\n' % (test_name,)
    run_tests_part1 += '    unittest.main()\n'
    output = '%s\n%s\n%s\n%s' % (imports, output, run_tests_part1, run_tests_part2)
    return output

def main():
    config_filename = sys.argv[1]
    config = imp.load_source('config', config_filename)
    unittesting_script = get_unittesting_script(config)
    print unittesting_script

if __name__ == '__main__':
    main()
