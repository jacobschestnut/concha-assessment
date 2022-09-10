import unittest
from src.views.session_requests import get_all_sessions


class TestCaseBase(unittest, TestCase):
    def assertTicks(self, session):
        #tests to make sure each session has 15 ticks, and those ticks are between -10.0 and -100.0
        if len(session['ticks']) < 15:
            raise AssertionError('There are less than 15 ticks in this session.')
        
        if len(session['ticks']) > 15:
            raise AssertionError('There are more than 15 ticks in this session.')
        
        ticks = session['ticks']
        for tick in ticks:
            if (tick > -10) or (tick < -100):
                raise AssertionError('Tick falls out of specified range (-100 through -10)')
                
    def assertSameId(self, session):
        #tests to make sure all session ids are unique
        compare_sessions = get_all_sessions()
        counter = 0
        for x in compare_sessions:
            if session['id'] == x['id']:
                counter += 1
                
        if counter > 1:
            raise AssertionError('There is more than one session with the same sessionId.')
        
    def assertStep_Count(self, session):
        #tests to make sure step_count is unique for each session, and the value is between 0-9.
        compare_sessions = get_all_sessions()
        counter = 0
        for x in compare_sessions:
            if session['step_count'] == x['step_count']:
                counter += 1
                
        if counter > 1:
            raise AssertionError('There is more than one session with the same step_count.')
        
        if not (session['step_count'] <= 9) and (session['step_count'] >= 0):
            raise AssertionError('step_count value must be between 0 and 9.')
        
    def assertSelected_Tick(self, session):
        #tests to make sure selected tick is between 1-15.
        if not (session['selected_tick'] <= 15) and (session['selected_tick'] >= 1):
            raise AssertionError('selected_tick value must be between 1 and 15.')
        
class TestSessionInfo(TestCaseBase):
    def test_data(self):
        #tests to make sure all user data exists
        sessions = get_all_sessions()
        for session in sessions:
            self.assertTicks(session)
            self.assertSameId(session)
            self.assertStep_Count(session)
            self.assertSelected_Tick(session)