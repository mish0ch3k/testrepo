def validate_user_access(user, context):
    """
    Complex function to test Cyclomatic Complexity.
    Has too many nested branches.
    """
    status = False
    if user:
        if user.get('is_active'):
            if user.get('role') == 'admin':
                if context.get('ip_address'):
                    if context['ip_address'].startswith('192.168'):
                        status = True
                    else:
                        if context.get('vpn_connected'):
                            status = True
                        else:
                            print("Invalid IP")
                else:
                    print("No IP context")
            elif user.get('role') == 'manager':
                if context.get('working_hours'):
                    if 9 <= context['current_hour'] <= 18:
                        status = True
                    else:
                        print("Outside working hours")
                else:
                    print("No time context")
            else:
                if user.get('has_pass'):
                    status = True
                else:
                    print("No pass")
        else:
            print("User inactive")
    else:
        print("No user")
    
    return status