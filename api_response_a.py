def schedule_appointment_helper(scope)
  contact_number = format_contact_number(params[:contact_number])  # Helper method for formatting
  user = AccountBlock::Account.find_by(phone_number: contact_number)

  conflicting_parties = BxBlockAppointmentManagement::ConflictingPartyDetail
                         .includes(:issue)
                         .where(contact_number: contact_number)
                         .map(&:issue).pluck('id')

  conflict_issues = BxBlockAppointmentManagement::Issue
                     .where(id: conflicting_parties)
                     .joins(:appointment_schedule)
                     .public_send(scope)  # Use `scope` for dynamic query (e.g., today, past, upcoming)

  users_data = user&.issues&.joins(:appointment_schedule)&.public_send(scope)

  # ... rest of the logic to build and render the JSON response ...
end

def today_schedule_appointment
  schedule_appointment_helper(:today)
end

# Similarly, define `past_schedule_appointment` and `upcoming_schedule_appointment`
# using the helper method with different scope values.
