package hello

type AdPlan struct {
	Name         string `value:"ad_plan"`
	SelectFields string `value:"account_id,name"`
}

type AdProject struct {
	Name         string `value:"ad_project"`
	SelectFields string `value:"id,plan_id"`
}
