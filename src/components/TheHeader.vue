<script>
import IconArrow from './icons/IconArrow.vue'
import IconLogo from './icons/IconLogo.vue'

export default {
  components: {
    IconArrow,
    IconLogo,
  },
}
</script>

<template>
  <div class="container header__wrapper">
    <nav class="header__nav">
      <ul class="header__list">
        <li class="header__item">
          <a href="/" class="header__link">Главная страница</a>
        </li>
        <!-- <li class="header__item">
          <a href="/about-us" class="header__link">О нас</a>
        </li> -->
        <li class="header__item">
          <a href="/events" class="header__link highlight-text bold">Мероприятия</a>
          <!-- <IconArrow direction="down" fill="#65B2DA"/> -->
        </li>
      </ul>
    </nav>
    <a href="" class="logo-link"><IconLogo class="logo-icon" /></a>
  </div>
</template>

<style>
:root {
  --logo-height: 50px;
}
</style>

<style scoped>
/* .logo-link {
  display: flex;
  align-items: center;
}

.logo-icon {
  height: 25px;
  width: 25px;
}

.header__wrapper {
  display: flex;
  justify-content: space-between;
  margin-top: 0.7rem;
  align-items: center;
}

.header__nav {
  display: flex;
  align-items: center;
}

.header__list {
  display: flex;
  gap: 1rem;
}


@media (min-width: 768px) {
  
}

@media (min-width: 768px) and (max-width: 1024px) {

}

@media (min-width: 1024px) {

} */
.header__wrapper {
  position: relative;
  display: flex;
  justify-content: space-between;
  margin-top: 0.7rem;
  height: var(--logo-height);
}

.header__nav {
  align-self: center;
}

.header__list {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.header__item:last-child {
  display: flex;
  gap: 10px;
}

.logo-icon {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  height: var(--logo-height);
}

.header__link {
  position: relative;
}

.header__link:hover {
  color: var(--main-color);
}

.header__link::after {
  content: '';
  position: absolute;
  bottom: -5px;
  left: 0;
  width: 0;
  height: 2px;
  background-color: var(--main-color);
  transition: width 0.3s ease;
}

.header__link:hover::after {
  width: 100%;
}

@media (min-width: 320px) and (max-width: 768px) {
  
}
</style>
