import unittest

from unittest.loader import makeSuite

from test_cases.Log_off import TestLogOff
from test_cases.go_to_players import TestGoToPlayers
from test_cases.login_to_the_system import TestLoginPage
from test_cases.chose_leg import TestChoseLeg
from test_cases.add_a_new_player_clear import TestAddANewPlayerClear
from test_cases.add_a_new_player import TestAddANewPlayer

def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestGoToPlayers))
   test_suite.addTest(makeSuite(TestLogOff))
   test_suite.addTest(makeSuite(TestLoginPage))
   test_suite.addTest(makeSuite(TestChoseLeg))
   test_suite.addTest(makeSuite(TestAddANewPlayerClear))
   test_suite.addTest(makeSuite(TestAddANewPlayer))
   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())
