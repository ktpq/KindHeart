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