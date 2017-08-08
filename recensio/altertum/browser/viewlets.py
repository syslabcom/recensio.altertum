from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from recensio.policy.browser.comments import CommentsViewlet as BaseCommentsViewlet


class CommentsViewlet(BaseCommentsViewlet):
    index = ViewPageTemplateFile('templates/comments.pt')
