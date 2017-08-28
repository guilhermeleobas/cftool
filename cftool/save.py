import os
import subprocess


def save(site_id, problem_id, data):
    """
    site_id: cf or uri or something that uniquely identifies the website
    problem_id: id of the problem. i.e. codeforces.com/contest/101/problem/A <---- id
    data looks like:
    {
        'in': [
            in_0,
            in_1,
            in_2, ...
        ],
        'out': [
            out_0,
            out_1,
            out_2, ...
        ]
    }
    """
    current_dir = os.getcwd()
    dir_name = os.path.join(os.getcwd(), site_id + problem_id)

    if (not os.path.exists(dir_name)):
        os.makedirs(dir_name)

    sz = len(data['in'])

    for i in range(sz):
        input_filename = os.path.join(dir_name, str(i) + '.in')
        output_filename = os.path.join(dir_name, str(i) + '.out')

        f_in = open(input_filename, 'w')
        f_out = open(output_filename, 'w')

        f_in.write(data['in'][i])
        f_out.write(data['out'][i])
