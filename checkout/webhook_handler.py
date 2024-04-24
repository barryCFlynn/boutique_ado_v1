from django.http import HttpeResponse

class StriepWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpeResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)