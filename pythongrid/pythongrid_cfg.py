"""configuration file for pythongrid"""
import os
import sys

def get_white_list():
    """
    parses output of qstat -f to get list of nodes
    """

    try:
        qstat = os.popen("qstat -f")

        node_names = []

        for line in qstat:

            if "@" in line:
                tokens = line.strip().split()
                node_name = tokens[0]

                if len(tokens) == 6:
                    continue

                node_names.append(node_name)

        qstat.close()

        return node_names

    except Exception, details:
        print "getting whitelist failed", details
        return ""


CFG = {}

# module path
path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)

# default python path
CFG['PYTHONPATH'] = ":".join(sys.path)

print CFG

CFG['PYGRID']     = dir_path + "/libpythongrid_wrapper.sh"
CFG['TEMPDIR']    = os.environ['HOME'] + "/tmp/"

# error emails
CFG['SEND_ERROR_MAILS'] = False
CFG['SMTPSERVER'] = "mailhost.myplace.org"
CFG['ERROR_MAIL_SENDER'] = "error@myplace.org"
CFG['ERROR_MAIL_RECIPIENT'] = "recepient@myplace.org"
CFG['MAX_MSG_LENGTH'] = 5000

# additional features

# plot cpu and mem usage and send via email
CFG['CREATE_PLOTS'] = False 

# enable web-interface to monitor jobs
CFG['USE_CHERRYPY'] = False 


# under the hood

# how much time can pass between heartbeats, before
# job is assummed to be dead in seconds
CFG['MAX_TIME_BETWEEN_HEARTBEATS'] = 90

# factor by which to increase the requested memory
# if an out of memory event was detected. 
CFG['OUT_OF_MEM_INCREASE'] = 2.0

# defines how many times can a particular job can die, 
# before we give up
CFG['NUM_RESUBMITS'] = 3

# check interval: how many seconds pass before we check
# on the status of a particular job in seconds
CFG['CHECK_FREQUENCY'] = 15

# heartbeat frequency: how many seconds pass before jobs
# on the cluster send back heart beats to the submission 
# host
CFG['HEARTBEAT_FREQUENCY'] = 10

# white-list of nodes to use
CFG['WHITELIST'] = get_white_list()

# black-list of nodes
CFG['BLACKLIST'] = []

# remove black-list from white-list
for node in CFG['BLACKLIST']:
    CFG['WHITELIST'].remove(node)


if __name__ == '__main__':

    for key, value in CFG.items():
        print '#'*30
        print key, value

