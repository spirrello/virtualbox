#!/usr/bin/env python

"""This script will restore guests from a snapshot and power them back on."""

#Commands to run
#VBoxManage controlvm c7-9 poweroff
#VBoxManage snapshot c7-9 restore snapshot1
#VBoxManage startvm c7-9 --type headless

import argparse
import subprocess
import time

#global var for list of guests
guest_list = ['c7-1','c7-2','c7-3','c7-4','c7-5','c7-6','c7-7','c7-8','c7-9']

def restore_vbox_guests():
    parser = argparse.ArgumentParser()
    parser.add_argument('-g','--guest', help='You can enter more than one but do not use commas to separate.', required='False', default='all')
    parser.add_argument('-s','--snapshot', help='Snapshot to restore', required='False', default='snapshot1')

    args = parser.parse_args()

    print(args)

    if args.guest == 'all':
        args.guest = guest_list
        print (args.guest)
    else:
        args.guest.replace(',', '')
        args.guest = args.guest.split()
    for guest in args.guest:
        print(type(guest))
        print(guest)
        time.sleep(2)
        subprocess.call(['VBoxManage', 'controlvm', guest.lower(), 'poweroff'])
        time.sleep(2)
        subprocess.call(['VBoxManage', 'snapshot', guest.lower(), 'restore', args.snapshot.lower()])
        time.sleep(2)
        subprocess.call(['VBoxManage','startvm', guest.lower(), '--type', 'headless'])
    

    # for vm in guests:
    #     if len(guests) != len(guest_list):




restore_vbox_guests()  
