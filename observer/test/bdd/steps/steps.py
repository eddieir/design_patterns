from lettuce import step
import sys
sys.path.insert(1,'/home/eddie/Desktop/python/DesignPatternPython/observer/observer')
from observer  import *
from nose.tools import assert_equal, assert_in

@step(u'Given I have a subject')
def given_i_have_a_subject(step):
  subject = Subject()

@step(u'When I "([^"]*)" subcribe in the subject')
def when_i_group1_subscribe_in_the_subject(step, name):
  subject = Subject()
  observer1 = USATimeObserver(name)
  subject.register_observer(observer1)
  assert_equal(1, len(subject.observers))

@step(u'Then I will be notified')
def then_i_will_be_notified(step):
  subject = Subject()
  observer1 = USATimeObserver('lorie')
  subject.register_observer(observer1)
  subject.notify_observers()
  assert (subject.cur_time != None)

@step(u'When I unsubscribe in the subject')
def when_i_group1_unsubscribe_in_the_subject(step):
  subject = Subject()
  observer1 = USATimeObserver('lorie')
  subject.register_observer(observer1)

  subject.unregister_observer(observer1)
  assert_equal (len(subject.observers), 0)

@step(u'Then I will not receive any notifications')
def then_i_will_not_receive_any_notifications(step):
  subject = Subject()
  observer1 = USATimeObserver('lorie')
  subject.register_observer(observer1)

  subject.unregister_observer(observer1)
  assert (subject.cur_time == None)