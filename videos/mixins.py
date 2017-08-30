from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator


class MemberRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        print("Requiring...?")
        obj = self.get_object()
        user = request.user
        if user.is_staff:
            return super(MemberRequiredMixin, self).dispatch(request, *args, **kwargs)
        if obj.free:
            return super(MemberRequiredMixin, self).dispatch(request, *args, **kwargs)
        return HttpResponse("Oops, not free!")


class StaffMemberRequired(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffMemberRequired, self).dispatch(request, *args, **kwargs)