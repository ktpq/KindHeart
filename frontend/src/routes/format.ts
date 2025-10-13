import { format } from "date-fns";

export const formatDate = (date: string) => {
  const d = new Date(date);
  return format(
    new Date(
      Date.UTC(d.getUTCFullYear(), d.getUTCMonth(), d.getUTCDate())
    ),
    "dd MMM yyyy"
  );
};

export const formatDateTime = (date: string) => {
  const d = new Date(date);
  return format(
    new Date(
      Date.UTC(d.getUTCFullYear(), d.getUTCMonth(), d.getUTCDate(), d.getUTCHours(), d.getUTCMinutes())
    ),
    "dd MMM yyyy, HH:mm"
  );
};

export const formatTimeUTC = (date: string) => {
  const d = new Date(date);
  let hours = d.getUTCHours();
  const minutes = String(d.getUTCMinutes()).padStart(2, "0");
  const ampm = hours >= 12 ? "PM" : "AM";
  hours = hours % 12;
  if (hours === 0) hours = 12; // 0 ชั่วโมง = 12 AM
  return `${hours}:${minutes} ${ampm}`;
};