from django.shortcuts import redirect

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Redirect to login if session has expired
        if request.path.startswith("/getclaim/") or request.path.startswith("/postAcnt/") or request.path.startswith("/getDisburseIds/") or request.path.startswith("/getDisburseRecords/") or request.path.startswith("/getFranchiseDisbursedRecords/") or request.path.startswith("/getFranchiseClaimed/") or request.path.startswith("/SettlementWindowViewSet/") or request.path.startswith("/DisburseViewsets/"):
            return self.get_response(request) 
        if not request.session.get('employee_id') and request.path != '/login/check/':
            return redirect('login_check')  # Replace 'login_page' with your login page URL name

        return self.get_response(request)

