def print_star_digits():
    star_digits={
        '2': ['    *  *   ', 
              '  *      * ',
              '  *       *',
              '   *     * ',
              '        *  ',
              '       *   ',
              '      *    ',
              '     *     ',
              '    *      ',
              '   *       ',
              '  * * * * *'],
        '3': ['    * * *   ',
              '  *       * ',
              '  *        *',
              '           *',
              '          * ',
              '    * * *   ',
              '          * ',
              '           *',
              '           *',
              ' *         *',
              '  *       * ',
              '    * * *   '],
        '5': ['   * * * * ',
              '   *       ',
              '   *       ',
              '   * * *   ',
              '         * ',
              '          *',
              '          *',
              '  *      * ',
              '   * * *   '] }
    number=input ("Введите число (2,3 или 5): ")         
    if number in star_digits:
            for line in star_digits[number]:
                    print(line)
    else:
            print("2,3 или 5.")
print_star_digits()
              
              
            


