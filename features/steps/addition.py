from behave import *


@given('we have two numbers')
def step_impl(context):
    context.x = 1
    context.y = 2


@when('we add them together')
def step_impl(context):
    context.result = context.x + context.y


@then('we should see the added numbers')
def step_impl(context):
    assert context.result == 3
