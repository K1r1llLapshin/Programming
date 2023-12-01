#include "Alphabet.h"

vector<vector<char>> Alphabet::Letters(char letter, char syb)
{
    char lettersUppercase[30][7][5] = {
        {
            {' ', syb, syb, syb, ' '},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb},
            {syb, syb, syb, syb, syb},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb}
        },
        {
            {syb, syb, syb, syb, syb},
            {syb, ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', ' ', ' '},
            {syb, syb, syb, syb, ' '},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb},
            {syb, syb, syb, syb, ' '}
        }, 
        {
            {syb, syb, syb, syb, ' '},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', syb, syb, ' '},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb},
            {syb, syb, syb, syb, ' '}
        },
        {
            {' ', syb, syb, syb, syb},
            {syb, ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', ' ', ' '}
        },
        {
            {' ', ' ', syb, syb, ' '},
            {' ', syb, ' ', syb, ' '},
            {' ', syb, ' ', syb, ' '},
            {' ', syb, ' ', syb, ' '},
            {' ', syb, ' ', syb, ' '},
            {syb, syb, syb, syb, syb},
            {syb, ' ', ' ', ' ', syb}
        },
        {
            {syb, syb, syb, syb, ' '},
            {syb, ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', ' ', ' '},
            {syb, syb, syb, ' ', ' '},
            {syb, ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', ' ', ' '},
            {syb, syb, syb, syb, ' '}
        },
        {
            {syb, ' ', syb, ' ', syb},
            {syb, ' ', syb, ' ', syb},
            {' ', syb, syb, syb, ' '},
            {' ', ' ', syb, ' ', ' '},
            {' ', syb, syb, syb, ' '},
            {syb, ' ', syb, ' ', syb},
            {syb, ' ', syb, ' ', syb}
        },
        {
            {' ', syb, syb, syb, ' '},
            {syb, ' ', ' ', ' ', syb},
            {' ', ' ', ' ', ' ', syb},
            {' ', ' ', syb, syb, ' '},
            {' ', ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb},
            {' ', syb, syb, syb, ' '}
        },
        {
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', syb, syb},
            {syb, ' ', syb, ' ', syb},
            {syb, syb, ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb}
        },
        {
            {' ', syb, syb, syb, ' '},
            {' ', ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', syb, syb},
            {syb, ' ', syb, ' ', syb},
            {syb, syb, ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb}
        },
        {
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', syb, ' ', ' '},
            {syb, syb, ' ', ' ', ' '},
            {syb, syb, ' ', ' ', ' '},
            {syb, ' ', syb, ' ', ' '},
            {syb, ' ', ' ', syb, ' '}
        },
        {
            {' ', ' ', syb, syb, syb},
            {' ', syb, ' ', ' ', syb},
            {' ', syb, ' ', ' ', syb},
            {' ', syb, ' ', ' ', syb},
            {' ', syb, ' ', ' ', syb},
            {' ', syb, ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb}
        },
        {
            {syb, ' ', ' ', ' ', syb},
            {syb, syb, ' ', syb, syb},
            {syb, ' ', syb, ' ', syb},
            {syb, ' ', syb, ' ', syb},
            {syb, ' ', syb, ' ', syb},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb}
        },
        {
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb},
            {syb, syb, syb, syb, syb},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb}
        },
        {
            {' ', syb, syb, syb, ' '},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb},
            {' ', syb, syb, syb, ' '}
        },
        {
            {' ', syb, syb, syb, ' '},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb}
        },
        {
            {' ', syb, syb, ' ', ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, syb, syb, ' ', ' '},
            {syb, ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', ' ', ' '}
        },
        {
            {' ', syb, syb, syb, ' '},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', ' ', syb},
            {' ', syb, syb, syb, ' '}
        },
        {
            {syb, syb, syb, syb, syb},
            {' ', ' ', syb, ' ', ' '},
            {' ', ' ', syb, ' ', ' '},
            {' ', ' ', syb, ' ', ' '},
            {' ', ' ', syb, ' ', ' '},
            {' ', ' ', syb, ' ', ' '},
            {' ', ' ', syb, ' ', ' '}
        },
        {
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
            {' ', syb, syb, syb, ' '},
            {' ', ' ', ' ', syb, ' '},
            {' ', syb, syb, ' ', ' '}
        },
        {
            {' ', ' ', syb, ' ', ' '},
            {' ', syb, syb, syb, ' '},
            {syb, ' ', syb, ' ', syb},
            {syb, ' ', syb, ' ', syb},
            {syb, ' ', syb, ' ', syb},
            {' ', syb, syb, syb, ' '},
            {' ', ' ', syb, ' ', ' '}
        },
        {
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb},
            {' ', syb, ' ', syb, ' '},
            {' ', ' ', syb, ' ', ' '},
            {' ', syb, ' ', syb, ' '},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb}
        },
        {
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
            {' ', syb, syb, syb, ' '},
            {' ', ' ', ' ', ' ', syb}
        },
        {
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb},
            {' ', syb, syb, syb, syb},
            {' ', ' ', ' ', ' ', syb},
            {' ', ' ', ' ', ' ', syb},
            {' ', ' ', ' ', ' ', syb}
        },
        {
            {syb, ' ', syb, ' ', syb},
            {syb, ' ', syb, ' ', syb},
            {syb, ' ', syb, ' ', syb},
            {syb, ' ', syb, ' ', syb},
            {syb, ' ', syb, ' ', syb},
            {syb, ' ', syb, ' ', syb},
            {' ', syb, syb, syb, syb}
        },
        {
            {syb, ' ', syb, ' ', syb},
            {syb, ' ', syb, ' ', syb},
            {syb, ' ', syb, ' ', syb},
            {syb, ' ', syb, ' ', syb},
            {syb, ' ', syb, ' ', syb},
            {' ', syb, syb, syb, syb},
            {' ', ' ', ' ', ' ', syb}
        },
        {
            {' ', syb, syb, syb, ' '},
            {syb, ' ', ' ', ' ', syb},
            {' ', ' ', ' ', ' ', syb},
            {' ', ' ', syb, syb, syb},
            {' ', ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb},
            {' ', syb, syb, syb, ' '}
        },
        {
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', syb, ' ', syb},
            {syb, ' ', syb, ' ', syb},
            {syb, syb, syb, ' ', syb},
            {syb, ' ', syb, ' ', syb},
            {syb, ' ', syb, ' ', syb},
            {syb, ' ', ' ', syb, ' '}
        },
        {
            {' ', syb, syb, syb, syb},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb},
            {' ', syb, syb, syb, syb},
            {' ', syb, ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb}
        },
        {
            {syb, ' ', ' ', syb, ' '},
            { ' ', ' ', ' ', ' ', ' ' },
            { syb, syb, syb, syb, ' ' },
            { syb, ' ', ' ', ' ', ' ' },
            { syb, syb, syb, ' ', ' ' },
            { syb, ' ', ' ', ' ', ' ' },
            { syb, syb, syb, syb, ' ' }
        }
    };
    char lettersLowercase[33][7][5] = {
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {' ', syb, syb, syb, ' '},
            {' ', ' ', ' ', ' ', syb},
            {' ', syb, syb, syb, syb},
            {syb, ' ', ' ', ' ', syb},
            {' ', syb, syb, syb, ' '},
        },       
        {
            {' ', ' ', ' ', syb, ' '},
            {' ', syb, syb, ' ', ' '},
            {syb, ' ', ' ', ' ', ' '},
            {syb, syb, syb, syb, ' '},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb},
            {' ', syb, syb, syb, ' '},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {syb, syb, syb, ' ', ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', syb, ' ', ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, syb, syb, ' ', ' '},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {syb, syb, syb, ' ', ' '},
            {syb, ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', ' ', ' '},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', syb, syb, ' '},
            {' ', syb, ' ', syb, ' '},
            {' ', syb, ' ', syb, ' '},
            {' ', syb, ' ', syb, ' '},
            {syb, syb, syb, syb, syb},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {' ', syb, syb, syb, ' '},
            {syb, ' ', ' ', ' ', syb},
            {syb, syb, syb, syb, ' '},
            {syb, ' ', ' ', ' ', ' '},
            {' ', syb, syb, syb, ' '},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {syb, ' ', syb, ' ', syb},
            {' ', syb, syb, syb, ' '},
            {' ', ' ', syb, ' ', ' '},
            {' ', syb, syb, syb, ' '},
            {syb, ' ', syb, ' ', syb},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {' ', syb, syb, ' ', ' '},
            {syb, ' ', ' ', syb, ' '},
            {' ', ' ', syb, ' ', ' '},
            {syb, ' ', ' ', syb, ' '},
            {' ', syb, syb, ' ', ' '},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', syb, syb, ' '},
            {syb, syb, ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
        },
        {
            {' ', syb, syb, ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', syb, syb, ' '},
            {syb, syb, ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', syb, ' ', ' '},
            {syb, syb, ' ', ' ', ' '},
            {syb, ' ', syb, ' ', ' '},
            {syb, ' ', ' ', syb, ' '},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', syb, syb, ' '},
            {' ', syb, ' ', syb, ' '},
            {' ', syb, ' ', syb, ' '},
            {' ', syb, ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {' ', syb, ' ', syb, ' '},
            {syb, ' ', syb, ' ', syb},
            {syb, ' ', syb, ' ', syb},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, syb, syb, syb, ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {' ', syb, syb, ' ', ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
            {' ', syb, syb, ' ', ' '},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {' ', syb, syb, ' ', ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', syb, syb, ' ', ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, syb, syb, ' ', ' '},
            {syb, ' ', ' ', ' ', ' '},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {' ', syb, syb, ' ', ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', syb, ' '},
            {' ', syb, syb, ' ', ' '},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {' ', syb, syb, syb, ' '},
            {' ', ' ', syb, ' ', ' '},
            {' ', ' ', syb, ' ', ' '},
            {' ', ' ', syb, ' ', ' '},
            {' ', ' ', syb, ' ', ' '},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
            {' ', syb, syb, syb, ' '},
            {' ', ' ', ' ', syb, ' '},
            {' ', syb, syb, ' ', ' '},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', syb, ' ', ' '},
            {' ', syb, syb, syb, ' '},
            {syb, ' ', syb, ' ', syb},
            {syb, ' ', syb, ' ', syb},
            {' ', syb, syb, syb, ' '},
            {' ', ' ', syb, ' ', ' '},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', ' ', syb},
            {' ', syb, ' ', syb, ' '},
            {' ', ' ', syb, ' ', ' '},
            {' ', syb, ' ', syb, ' '},
            {syb, ' ', ' ', ' ', syb},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
            {' ', syb, syb, syb, ' '},
            {' ', ' ', ' ', ' ', syb},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
            {' ', syb, syb, syb, ' '},
            {' ', ' ', ' ', syb, ' '},
            {' ', ' ', ' ', syb, ' '},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {syb, ' ', syb, ' ', syb},
            {syb, ' ', syb, ' ', syb},
            {syb, ' ', syb, ' ', syb},
            {syb, ' ', syb, ' ', syb},
            {' ', syb, syb, syb, syb},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {syb, ' ', syb, ' ', syb},
            {syb, ' ', syb, ' ', syb},
            {syb, ' ', syb, ' ', syb},
            {syb, ' ', syb, ' ', syb},
            {' ', syb, syb, syb, syb},
            {' ', ' ', ' ', ' ', syb},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', ' ', ' '},
            {' ', syb, ' ', ' ', ' '},
            {' ', syb, syb, syb, ' '},
            {' ', syb, ' ', ' ', syb},
            {' ', syb, syb, syb, ' '},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', ' ', syb},
            {syb, ' ', ' ', ' ', syb},
            {syb, syb, syb, ' ', syb},
            {syb, ' ', ' ', syb, syb},
            {' ', syb, syb, ' ', syb},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', ' ', ' '},
            {syb, syb, syb, ' ', ' '},
            {syb, ' ', ' ', syb, ' '},
            {' ', syb, syb, ' ', ' '},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {' ', syb, syb, ' ', ' '},
            {syb, ' ', ' ', syb, ' '},
            {' ', ' ', syb, syb, ' '},
            {syb, ' ', ' ', syb, ' '},
            {' ', syb, syb, ' ', ' '},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', syb, ' ', syb},
            {syb, syb, syb, ' ', syb},
            {syb, ' ', syb, ' ', syb},
            {syb, ' ', ' ', syb, ' '},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {' ', syb, syb, ' ', ' '},
            {syb, ' ', ' ', syb, ' '},
            {syb, ' ', ' ', syb, ' '},
            {' ', syb, syb, syb, ' '},
            {syb, ' ', ' ', syb, ' '},
        },
        {
            {' ', syb, ' ', syb, ' '},
            {' ', ' ', ' ', ' ', ' '},
            {' ', syb, syb, syb, ' '},
            {syb, ' ', ' ', ' ', syb},
            {syb, syb, syb, syb, ' '},
            {syb, ' ', ' ', ' ', ' '},
            {' ', syb, syb, syb, ' '},
        }

    };
    char symbol[5][7][5] = {
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
        },
        {
            {' ', syb, syb, ' ', ' '},
            {syb, ' ', ' ', syb, ' '},
            {' ', ' ', ' ', syb, ' '},
            {' ', ' ', syb, ' ', ' '},
            {' ', syb, ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {' ', syb, ' ', ' ', ' '},
        },
        {
            {' ', syb, ' ', ' ', ' '},
            {' ', syb, ' ', ' ', ' '},
            {' ', syb, ' ', ' ', ' '},
            {' ', syb, ' ', ' ', ' '},
            {' ', syb, ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {' ', syb, ' ', ' ', ' '},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {syb, syb, syb, syb, syb},
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
        },
        {
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {' ', ' ', ' ', ' ', ' '},
            {syb, syb, ' ', ' ', ' '},
            {syb, syb, ' ', ' ', ' '},
        },

    };
    int num_letter;

    switch (letter)
    {
    case 'Ý':
        num_letter = 26;
        break;
    case 'Þ':
        num_letter = 27;
        break;
    case 'ß':
        num_letter = 28;
        break;
    case '¨':
        num_letter = 29;
        break;
    case '¸':
        num_letter = 64;
        break;
    default:
        num_letter = letter + 64;
        break;
    }

    vector<vector<char>> ch(7,vector<char>(5));
    if (num_letter >= 0 && num_letter < 30)
    {
        for (int i = 0; i < 7; ++i)
            for (int j = 0; j < 5; ++j)
                ch[i][j] = lettersUppercase[num_letter][i][j];
    }
    else if (num_letter >= 32 && num_letter <= 64)
    {
        num_letter = num_letter - 32;
        for (int i = 0; i < 7; ++i)
            for (int j = 0; j < 5; ++j)
                ch[i][j] = lettersLowercase[num_letter][i][j];
    }
    else
    {
        switch (letter)
        {
        case ' ':
            num_letter = 0;
            break;
        case '?':
            num_letter = 1;
            break;
        case '!':
            num_letter = 2;
            break;
        case '-':
            num_letter = 3;
            break;
        case '.':
            num_letter = 4;
            break;
        }
        for (int i = 0; i < 7; ++i)
            for (int j = 0; j < 5; ++j)
                ch[i][j] = symbol[num_letter][i][j];
    }
    return ch;
}
vector<vector<char>> Alphabet::GivenLetter(char letter, char symbol)
{
    vector<vector<char>> given_letter;
    given_letter = Letters(letter, symbol);
    return given_letter;
}

void Alphabet::PrintText(string text, char symbol, string color, int y, int x)
{
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);

    vector<vector<vector<char>>> ch;
    for (char letter : text)
        ch.push_back(GivenLetter(letter, symbol));

    for (int i = 0; i < y; i++)
        cout << '\n';
    

    SetConsoleTextAttribute(hConsole, GetColor(color));
    for (int j = 0; j < 7; j++)
    {
        for (int i = 0; i < x; i++)
            cout << ' ';
        for (int i = 0; i < ch.size(); i++)
        {
            for (int k = 0; k < 5; k++)
                cout << ch[i][j][k];
            cout << ' ';
        }
        cout << '\n';
    }
    SetConsoleTextAttribute(hConsole, 0);
}
int Alphabet::GetColor(string color)
{
    if (color == "Black")
        return 0;
    else if (color == "Blue")
        return FOREGROUND_BLUE;
    else if (color == "Green") 
        return FOREGROUND_GREEN;
    else if (color == "Cyan") 
        return FOREGROUND_GREEN | FOREGROUND_BLUE;
    else if (color == "Red")
        return FOREGROUND_RED;
    else if (color == "Magenta")
        return FOREGROUND_RED | FOREGROUND_BLUE;
    else if (color == "Yellow") 
        return FOREGROUND_RED | FOREGROUND_GREEN;
    else if (color == "White")
        return FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE;

    return 0;
}


