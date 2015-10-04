# this is the simplest python program
import Team1
import Team2
import Team3
import Team4
import Team5
import Team6
import Team7
import Team8
import Team9
import Team10

def main():
    plain_text = "8803 ASE is the most incredible class of all time."
    print "PLAIN TEXT: " + plain_text
    temp_text = Team1.encrypt(plain_text)
    print "TEAM 1 ENCRYPTED: " + temp_text
    temp_text = Team2.encrypt(temp_text)
    print "TEAM 2 ENCRYPTED: " + temp_text
    temp_text = Team3.encrypt(temp_text)
    print "TEAM 3 ENCRYPTED: " + temp_text
    temp_text = Team4.encrypt(temp_text)
    print "TEAM 4 ENCRYPTED: " + temp_text
    temp_text = Team5.encrypt(temp_text)
    print "TEAM 5 ENCRYPTED: " + temp_text
    temp_text = Team6.encrypt(temp_text)
    print "TEAM 6 ENCRYPTED: " + temp_text
    temp_text = Team7.encrypt(temp_text)
    print "TEAM 7 ENCRYPTED: " + temp_text
    temp_text = Team8.encrypt(temp_text)
    print "TEAM 8 ENCRYPTED: " + temp_text
    temp_text = Team9.encrypt(temp_text)
    print "TEAM 9 ENCRYPTED: " + temp_text
    temp_text = Team10.encrypt(temp_text)
    print "TEAM 10 ENCRYPTED: " + temp_text
    
    
    
    print ""
    print ""
    print "FINAL ENCRYPTED TEXT: " + temp_text
    print ""
    print ""
    
    
    
    temp_text = Team10.decrypt(temp_text)
    print "TEAM 10 DECRYPTED: " + temp_text
    temp_text = Team9.decrypt(temp_text)
    print "TEAM 9 DECRYPTED: " + temp_text
    temp_text = Team8.decrypt(temp_text)
    print "TEAM 8 DECRYPTED: " + temp_text
    temp_text = Team7.decrypt(temp_text)
    print "TEAM 7 DECRYPTED: " + temp_text
    temp_text = Team6.decrypt(temp_text)
    print "TEAM 6 DECRYPTED: " + temp_text
    temp_text = Team5.decrypt(temp_text)
    print "TEAM 5 DECRYPTED: " + temp_text
    temp_text = Team4.decrypt(temp_text)
    print "TEAM 4 DECRYPTED: " + temp_text
    temp_text = Team3.decrypt(temp_text)
    print "TEAM 3 DECRYPTED: " + temp_text
    temp_text = Team2.decrypt(temp_text)
    print "TEAM 2 DECRYPTED: " + temp_text
    temp_text = Team1.decrypt(temp_text)
    print "TEAM 1 DECRYPTED: " + temp_text
    
    print ""
    print ""
    print "FINAL MESSAGE: " + temp_text
    print ""
    print ""

main()

# click the 'Run' button at the top to start this application
