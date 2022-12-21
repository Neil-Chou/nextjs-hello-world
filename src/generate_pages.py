import os
import argparse
import datetime

def process_subpage(time_now, args):

    now = time_now['now']
    now_ori = time_now['now_ori']
    
    current_folder_path = os.path.dirname(os.path.realpath(__file__))

    current_date_folder = current_folder_path + "/../pages" + '/' + now
    if not os.path.exists(current_date_folder):
        os.makedirs(current_date_folder)

    files = os.listdir(args.folder)
    if ".DS_Store" in files:
        files.remove(".DS_Store")  

    content = dict()
    for file in files:
        with open(args.folder + '/' + file) as file_read:
            lines = file_read.readlines()
            text = ''.join(lines)
            text = text.replace('\n', '')
            text = text.replace('<br></br>', '<br></br><br></br>')
            text = text.replace("<!DOCTYPE html>", '')
            content[file.split('.html')[0]] = text
    print(content)





    # generate index.js
    with open(current_date_folder + '/' + 'index.js', 'w') as file_write:
        first =  \
            """
import Link from 'next/link'
const """+ 'V' + str(int(now_ori.timestamp())) + """ = () =>( 
    
    <html><Link href="/">
            <a><big>Back</big></a>
        </Link><br></br><br></br>"""
        second = ""
        for key, value in content.items():
            # file_write.writelines()
            each = \
"""
<br></br>
<Link href="""+ '"/' + now + '/' + str(key) + '"' +""">
            <a>""" + str(key) + """</a>
        </Link>"""
            second += each
        last = \
"""
</html>
);
export default """ + 'V' + str(int(now_ori.timestamp())) + """;

            """
        final = first + second + last
        file_write.writelines(final)



    for key, value in content.items():

        # current_k_folder = current_date_folder + '/' + str(key)
        # if not os.path.exists(current_k_folder):
        #     os.makedirs(current_k_folder)
            
        with open(current_date_folder + '/' + str(key) + '.js', 'w') as file_write:
            a = \
            """
import Link from 'next/link'
const """+ 'V' + str(int(now_ori.timestamp())) + '_' + str(key) + """ = () =>( 
    
    <html>
        <Link href="""+ '"/' + now + '"' +""">
            <a><big>Back</big></a>
        </Link>""" + value +\
"""</html>
);
export default """ + 'V' + str(int(now_ori.timestamp())) + '_' + str(key) + """;

            """
            file_write.writelines(a)



    

def process_mainpage(time_now, args):


    now = time_now['now']
    now_ori = time_now['now_ori']
    
    current_folder_path = os.path.dirname(os.path.realpath(__file__))

    content = dict()

    with open(current_folder_path + '/../pages/index.js') as file_read:
        lines = file_read.readlines()

    title = "Name of folder is the UTC time when it generates.{' '}"
    with open(current_folder_path + '/../pages/index.js', 'w') as file_write:
        for line in lines:
            file_write.writelines(line)
            if title in line:
                file_write.writelines("    <br></br>\n")
                file_write.writelines('      <Link href="/' + now + '">\n')
                file_write.writelines('        <a>"/' + now + '"</a>\n')
                file_write.writelines("      </Link>\n")

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--folder', type=str, required=False, help="the input read folder", default="html")
    args = parser.parse_args()
    
    now_ori = datetime.datetime.utcnow()
    now = str(now_ori).replace(' ', '_').split('.')[0]
    time_now = {"now":now, "now_ori":now_ori}
    process_subpage(time_now, args)
    process_mainpage(time_now, args)
    


