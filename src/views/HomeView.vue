<script>
import HeroSection from '@/components/sections/HeroSection.vue'
import FuncsSections from '@/components/sections/FuncsSection.vue'
import AdvantagesSection from '@/components/sections/AdvantagesSection.vue'
import WorkflowSection from '@/components/sections/WorkflowSection.vue'
import FAQSection from '@/components/sections/FAQSection.vue'
import ContactsSection from '@/components/sections/ContactsSection.vue'
import STASection from '@/components/sections/STASection.vue'

export default {
  components: {
    HeroSection,
    FuncsSections,
    AdvantagesSection,
    WorkflowSection,
    FAQSection,
    ContactsSection,
    STASection,
  },
}
</script>

<template>
  <HeroSection />
  <FuncsSections />
  <AdvantagesSection />
  <WorkflowSection />
  <FAQSection />
  <ContactsSection />
  <STASection />
</template>

<style scoped></style>
